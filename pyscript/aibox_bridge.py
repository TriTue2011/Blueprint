"""AIBox WebSocket Bridge - Dual Mode: XiaoZhi & Server Việt"""
import json

DEFAULT_AIBOX_IP = "172.16.10.16"
DEFAULT_AIBOX_PORT = 8082

# ============================================
# SERVICE 1: XIAOZHI (Gửi 1 lần)
# ============================================

@service
def xiaozhi_speak(text=None, aibox_ip=None, aibox_port=None):
    """Gửi tin nhắn cho AIBox XiaoZhi (server Trung Quốc)
    
    Đặc điểm: Gửi 1 lần duy nhất
    
    Args:
        text: Nội dung cần nói
        aibox_ip: IP của AIBox (mặc định "172.16.10.16")
        aibox_port: Port (mặc định 8082)
    
    Cách dùng:
        service: pyscript.xiaozhi_speak
        data:
          text: "你好"
    """
    if not text:
        log.error("❌ No text")
        return False
    
    # Defaults
    if aibox_ip is None:
        aibox_ip = DEFAULT_AIBOX_IP
    if aibox_port is None:
        aibox_port = DEFAULT_AIBOX_PORT
    
    try:
        import websocket
        
        log.info(f"🔊 XiaoZhi: {text}")
        log.info(f"📡 AIBox: {aibox_ip}:{aibox_port}")
        
        ws_url = f"ws://{aibox_ip}:{aibox_port}"
        ws = websocket.WebSocket()
        ws.settimeout(5)
        ws.connect(ws_url)
        
        # Gửi 1 lần duy nhất
        payload = {"action": "chat_send_text", "text": str(text)}
        ws.send(json.dumps(payload, ensure_ascii=False))
        
        ws.close()
        log.info("✅ Done")
        return True
        
    except Exception as e:
        log.error(f"❌ Error: {e}")
        return False


# ============================================
# SERVICE 2: SERVER VIỆT (Smart - Detect state)
# ============================================

def send_and_detect_state(text, aibox_ip, aibox_port, max_wait=3.0):
    """Send text and detect if session needs wake
    
    Returns:
        ("idle", ws) = Session was idle, saw state change, now listening, ws still open
        ("active", None) = Session was active, NO state change
        ("error", None) = Error
    """
    import websocket
    ws = None
    try:
        ws_url = f"ws://{aibox_ip}:{aibox_port}"
        ws = websocket.WebSocket()
        ws.settimeout(5)
        ws.connect(ws_url)
        
        # Send text
        payload = {"action": "chat_send_text", "text": str(text)}
        ws.send(json.dumps(payload, ensure_ascii=False))
        log.info(f"📤 Sent: {text}")
        
        saw_state_change = False
        saw_listening = False
        
        # Read responses
        import time
        start_time = time.time()
        while (time.time() - start_time) < max_wait:
            try:
                ws.settimeout(0.2)
                data = json.loads(ws.recv())
                
                if data.get("type") == "chat_state":
                    state = data.get("state")
                    saw_state_change = True
                    
                    if state == "connecting":
                        log.info("🔴 State: connecting")
                        
                    elif state == "listening":
                        saw_listening = True
                        log.info("🟢 State: listening")
                        # Keep ws open
                        return ("idle", ws)
                        
            except:
                pass
        
        # KHÔNG CÓ state change = session đang active
        if not saw_state_change:
            log.info("✅ KHÔNG CÓ state change → Session ACTIVE")
            ws.close()
            return ("active", None)
        
        # Saw state but timeout
        ws.close()
        return ("error", None)
        
    except Exception as e:
        log.error(f"❌ Error: {e}")
        if ws:
            try:
                ws.close()
            except:
                pass
        return ("error", None)


@service
def aibox_speak(text=None, aibox_ip=None, aibox_port=None, post_listening_delay=None):
    """Gửi tin nhắn cho AIBox Server Việt
    
    Đặc điểm: Smart detect - Chỉ gửi 2 lần khi thấy state change
    
    Args:
        text: Nội dung cần nói
        aibox_ip: IP của AIBox (mặc định "172.16.10.16")
        aibox_port: Port (mặc định 8082)
        post_listening_delay: Delay sau listening (mặc định 3.0s)
    
    Flow:
        - KHÔNG CÓ state change → Session ACTIVE → Gửi 1 lần ✅ (AIBox nói luôn)
        - CÓ state change → Session IDLE → Gửi lần 1 (wake) → Đợi 3s → Gửi lần 2 ✅
    
    Cách dùng:
        service: pyscript.aibox_speak
        data:
          text: "Xin chào"
    """
    if not text:
        log.error("❌ No text")
        return False
    
    # Defaults
    if aibox_ip is None:
        aibox_ip = DEFAULT_AIBOX_IP
    if aibox_port is None:
        aibox_port = DEFAULT_AIBOX_PORT
    if post_listening_delay is None:
        post_listening_delay = 3.0
    else:
        post_listening_delay = float(post_listening_delay)
    
    try:
        log.info(f"🔊 Server Việt: {text}")
        log.info(f"📡 AIBox: {aibox_ip}:{aibox_port}")
        
        # Send and detect state
        status, ws = send_and_detect_state(text, aibox_ip, aibox_port)
        
        if status == "active":
            # KHÔNG CÓ state change → Session đang ACTIVE → AIBox sẽ nói luôn
            log.info("✅ Done (no state change - AIBox will speak)")
            return True
            
        elif status == "idle":
            # CÓ state change → Session vừa wake → Cần resend
            log.info(f"⏳ Saw state change, waiting {post_listening_delay}s...")
            task.sleep(post_listening_delay)
            
            log.info(f"📤 Resending: {text}")
            try:
                payload = {"action": "chat_send_text", "text": str(text)}
                ws.send(json.dumps(payload, ensure_ascii=False))
                ws.close()
                log.info("✅ Done (resent after state change)")
                return True
            except Exception as e:
                log.error(f"❌ Resend failed: {e}")
                try:
                    ws.close()
                except:
                    pass
                return False
        else:
            log.error("❌ Failed")
            return False
            
    except Exception as e:
        log.error(f"❌ Error: {e}")
        return False