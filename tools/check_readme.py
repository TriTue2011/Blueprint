"""Soát README có khớp với các file blueprint thật hay không.

Trình soát này đọc chính các file YAML rồi đối chiếu với những gì README nói về
chúng. Nó bắt đúng loại sai lệch mà mắt người bỏ qua vì README quá dài:

1. Bảng thông tin của một mục khai sai ``Loại`` (Script / Automation) so với
   ``blueprint.domain`` trong file.
2. Bảng thông tin khai sai ``HA tối thiểu`` so với ``homeassistant.min_version``.
3. Nút Import trỏ vào một file không tồn tại.
4. Có file YAML trong kho nhưng README không hề nhắc tới.
5. Liên kết mục lục trỏ vào một tiêu đề không có thật.

Chạy: ``python tools/check_readme.py``  (thêm đường dẫn kho nếu chạy từ nơi khác)
Trả 0 nếu sạch, 1 nếu có sai lệch.
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.parse
from pathlib import Path

# README tiếng Việt và tiếng Anh dùng nhãn khác nhau cho cùng một hàng.
NHAN_LOAI = ("Loại", "Type")
NHAN_PHIEN_BAN = ("HA tối thiểu", "HA minimum")

RE_TIEU_DE = re.compile(r"^(#{1,6}) (.+)$", re.M)
RE_HANG = re.compile(r"^\|\s*\*\*(.+?)\*\*\s*\|(.+?)\|\s*$", re.M)
RE_IMPORT = re.compile(r"blueprint_url=([^)\s]+)")
RE_LIEN_KET = re.compile(r"\]\((#[^)]+)\)")
RE_PHIEN_BAN = re.compile(r"\d{4}\.\d+\.\d+")


def doc_blueprint(duong_dan: Path) -> tuple[str, str]:
    """Lấy (domain, min_version) từ một file blueprint, không cần thư viện YAML.

    Chỉ đọc hai khoá phẳng nằm trong khối ``blueprint:`` nên không phải nạp cả
    file qua YAML — tránh kéo thêm phụ thuộc chỉ để đọc hai dòng.
    """
    domain = ""
    min_version = ""
    trong_blueprint = False
    for dong in duong_dan.read_text(encoding="utf-8").splitlines():
        if dong.startswith("blueprint:"):
            trong_blueprint = True
            continue
        if trong_blueprint and dong and not dong.startswith((" ", "\t")):
            break  # đã ra khỏi khối blueprint:
        if not trong_blueprint:
            continue
        m = re.match(r"^  domain:\s*(\S+)", dong)
        if m:
            domain = m.group(1).strip()
        m = re.match(r"^\s+min_version:\s*(\S+)", dong)
        if m:
            min_version = m.group(1).strip().strip("'\"")
    return domain, min_version


def neo(tieu_de: str) -> str:
    """Dựng neo kiểu GitHub cho một tiêu đề.

    GitHub bỏ emoji và dấu câu, hạ chữ thường, đổi khoảng trắng thành gạch nối,
    nhưng GIỮ ký tự biến thể U+FE0F — nên tiêu đề có emoji dạng ``🖼️`` sinh ra
    neo bắt đầu bằng ký tự vô hình đó. Đây là chỗ liên kết mục lục hay hỏng.
    """
    ra = []
    for ch in tieu_de.strip().lower():
        if ch == "️":
            ra.append(ch)
        elif ch.isalnum() or ch in "-_":
            ra.append(ch)
        elif ch.isspace():
            ra.append("-")
    return "".join(ra)


def tach_muc(noi_dung: str) -> list[tuple[str, str]]:
    """Cắt README thành các mục cấp ``##``, trả về [(tiêu đề, thân)]."""
    vi_tri = [(m.start(), m.group(2)) for m in RE_TIEU_DE.finditer(noi_dung)
              if m.group(1) == "##"]
    muc = []
    for i, (bat_dau, tieu_de) in enumerate(vi_tri):
        ket_thuc = vi_tri[i + 1][0] if i + 1 < len(vi_tri) else len(noi_dung)
        muc.append((tieu_de, noi_dung[bat_dau:ket_thuc]))
    return muc


def soat_mot_readme(readme: Path, kho: Path, files: set[str]) -> list[str]:
    loi: list[str] = []
    noi_dung = readme.read_text(encoding="utf-8")
    ten = readme.name

    # --- liên kết mục lục ---
    hop_le = {neo(m.group(2)) for m in RE_TIEU_DE.finditer(noi_dung)}
    for lk in sorted(set(RE_LIEN_KET.findall(noi_dung))):
        if lk[1:] not in hop_le:
            loi.append(f"{ten}: liên kết mục lục '{lk}' không trỏ tới tiêu đề nào")

    da_nhac: set[str] = set()

    for tieu_de, than in tach_muc(noi_dung):
        lien_ket = []
        for m in RE_IMPORT.finditer(than):
            lien_ket.append(urllib.parse.unquote(m.group(1)).rsplit("/", 1)[-1])
        if not lien_ket:
            continue
        da_nhac.update(lien_ket)

        thieu = [f for f in lien_ket if f not in files]
        for f in thieu:
            loi.append(f"{ten} · mục '{tieu_de}': nút Import trỏ vào '{f}' — không có file này")
        co_that = [f for f in lien_ket if f in files]
        if not co_that:
            continue

        hang = {k.strip(): v.strip() for k, v in RE_HANG.findall(than)}
        khai_loai = next((hang[k] for k in NHAN_LOAI if k in hang), None)
        khai_phien_ban = next((hang[k] for k in NHAN_PHIEN_BAN if k in hang), None)

        for f in co_that:
            domain, min_version = doc_blueprint(kho / f)
            if khai_loai is not None and domain and domain.lower() not in khai_loai.lower():
                loi.append(f"{ten} · mục '{tieu_de}': khai Loại '{khai_loai}' "
                           f"nhưng {f} có domain '{domain}'")
            if khai_phien_ban is not None and min_version:
                cac_ban = set(RE_PHIEN_BAN.findall(khai_phien_ban))
                if cac_ban and min_version not in cac_ban:
                    loi.append(f"{ten} · mục '{tieu_de}': khai HA tối thiểu "
                               f"'{khai_phien_ban}' nhưng {f} khai '{min_version}'")

    for f in sorted(files - da_nhac):
        loi.append(f"{ten}: file '{f}' có trong kho nhưng README không nhắc tới")

    return loi


def main() -> int:
    p = argparse.ArgumentParser(description="Soát README có khớp file blueprint không.")
    p.add_argument("kho", nargs="?", default=".", help="Thư mục kho (mặc định: thư mục hiện tại)")
    tham_so = p.parse_args()

    kho = Path(tham_so.kho).resolve()
    files = {f.name for f in kho.glob("*.yaml")}
    if not files:
        print(f"Không thấy file .yaml nào trong {kho}", file=sys.stderr)
        return 1

    readmes = [kho / n for n in ("README.md", "README.en.md") if (kho / n).exists()]
    if not readmes:
        print(f"Không thấy README nào trong {kho}", file=sys.stderr)
        return 1

    print("=" * 55)
    print("   Soát README so với file blueprint thật")
    print("=" * 55)
    print(f"{len(files)} blueprint · {len(readmes)} README\n")

    tat_ca: list[str] = []
    for r in readmes:
        loi = soat_mot_readme(r, kho, files)
        tat_ca.extend(loi)
        print(f"  [{'FAIL' if loi else 'PASS'}] {r.name}"
              + (f" — {len(loi)} sai lệch" if loi else ""))

    if tat_ca:
        print()
        for l in tat_ca:
            print(f"    • {l}")
    print("\n" + "-" * 55)
    print(f"Kết quả: {len(tat_ca)} sai lệch")
    print("-" * 55)
    return 1 if tat_ca else 0


if __name__ == "__main__":
    sys.exit(main())
