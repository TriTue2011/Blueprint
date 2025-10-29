# Hướng dẫn cài đặt thông báo khi các thiết bị mất kết nối

## Bước 1: Tạo một thực thể lưu trữ thông tin toàn bộ thiết bị đang bị mất kết nối

### Tạo một nhãn đặt tên là **Ignored**

![image](images/20250426_GwdtEl.png)

### Gán nhãn **Ignored** cho các thực thể không muốn theo dõi mất kết nối, để loại trừ chúng khỏi danh sách theo dõi

![image](images/20250426_oj1S9U.png)

### Tạo một template binary_sensor, thêm vào trong cấu hình `config/configuration.yaml`

``` yaml
template:
  - binary_sensor:
      - name: Unavailable Devices
        unique_id: unavailable_devices
        device_class: problem
        icon: >-
          {{ iif((this.attributes.raw | default([], true) | count > 0), 'mdi:alert-circle', 'mdi:check-circle') }}
        state: >-
          {{ this.attributes.raw | default([], true) | count > 0 }}
        attributes:
          devices: >-
            {{ this.attributes.raw | default([], true) | map('device_id') | reject('none') | unique | map('device_attr', 'name') | list }}
          entities: >-
            {{ this.attributes.raw | default([], true) }}
          raw: >-
            {% set ignored_label = 'ignored' -%} {% set ignored_domains = ['button'] -%}
            {% set ignored_integrations = ['demo', 'private_ble_device'] -%}
            {% set ignored_integration_entities = namespace(entities=[]) -%}
            {% for integration in ignored_integrations -%}
              {% set ignored_integration_entities.entities = ignored_integration_entities.entities + integration_entities(integration) -%}
            {% endfor -%}
            {% set ignored_devices = label_devices(ignored_label) -%}
            {% set ignored_device_entities = namespace(entities=[]) -%}
            {% for device in ignored_devices -%}
              {% set ignored_device_entities.entities = ignored_device_entities.entities + device_entities(device) -%}
            {% endfor -%}
            {% set ignored_individual_entities = label_entities(ignored_label) -%}
            {{ states
              | selectattr('state', 'in', ['unavailable'])
              | rejectattr('domain', 'in', ignored_domains)
              | rejectattr('entity_id', 'in', ignored_integration_entities.entities)
              | rejectattr('entity_id', 'in', ignored_device_entities.entities)
              | rejectattr('entity_id', 'in', ignored_individual_entities)
              | map(attribute='entity_id')
              | list }}
```

### Khởi động lại Home Assistant

## Bước 2: Tạo tự động thông báo. Thông báo sẽ tự động được ẩn sau khi thiết bị kết nối trở lại

### Tùy chọn thông báo qua giao diện Home Assistant

```yaml
alias: Thông báo khi có thiết bị mất kết nối
description: ""
triggers:
  - trigger: state
    entity_id:
      - binary_sensor.unavailable_devices
    attribute: entities
conditions:
  - condition: template
    value_template: "{{ trigger.from_state.state not in ['unavailable', 'unknown'] }}"
  - condition: template
    value_template: "{{ trigger.to_state.state not in ['unavailable', 'unknown'] }}"
actions:
  - variables:
      entities: "{{ state_attr(trigger.entity_id, 'entities') | default([], true) }}"
      devices: "{{ state_attr(trigger.entity_id, 'devices') | default([], true) }}"
      notify_tag: "{{ 'tag_' ~ this.attributes.id }}"
  - if:
      - condition: template
        value_template: "{{ entities | count > 0 }}"
    then:
      - action: persistent_notification.create
        data:
          notification_id: "{{ notify_tag }}"
          message: >
            ### Có {{ devices | count }} thiết bị ({{ entities | count }} thực
            thể) đang bị mất kết nối.

            {% for device in devices %}- ***{{ device }}***

            {% endfor %}{% for entity in entities %}  - *{{ entity }}*

            {% endfor %}
    else:
      - action: persistent_notification.dismiss
        data:
          notification_id: "{{ notify_tag }}"
mode: queued
max: 10
```

### Tùy chọn thông báo qua điện thoại

```yaml
alias: Thông báo khi có thiết bị mất kết nối
description: ""
triggers:
  - trigger: state
    entity_id:
      - binary_sensor.unavailable_devices
    attribute: entities
conditions:
  - condition: template
    value_template: "{{ trigger.from_state.state not in ['unavailable', 'unknown'] }}"
  - condition: template
    value_template: "{{ trigger.to_state.state not in ['unavailable', 'unknown'] }}"
actions:
  - variables:
      entities: "{{ state_attr(trigger.entity_id, 'entities') | default([], true) }}"
      devices: "{{ state_attr(trigger.entity_id, 'devices') | default([], true) }}"
      notify_tag: "{{ 'tag_' ~ this.attributes.id }}"
  - if:
      - condition: template
        value_template: "{{ entities | count > 0 }}"
    then:
      - action: notify.all_mobiles
        data:
          title: Mất kết nối thiết bị
          message: >-
            Có {{ devices | count }} thiết bị ({{ entities | count }} thực thể)
            đang bị mất kết nối.
          data:
            tag: "{{ notify_tag }}"
    else:
      - action: notify.all_mobiles
        data:
          message: clear_notification
          data:
            tag: "{{ notify_tag }}"
mode: queued
max: 10
```

## Bước 3: Tùy chọn hiển thị thẻ ở giao diện Home Assistant

### Tạo thẻ Markdown chỉ hiển thị khi có thiết bị mất kết nối

```yaml
type: markdown
content: >
  {% set entities = state_attr('binary_sensor.unavailable_devices', 'entities')
  | default([], true) -%}

  {% set devices = state_attr('binary_sensor.unavailable_devices', 'devices') |
  default([], true) -%}


  ### Có {{ devices | count }} thiết bị ({{ entities | count }} thực thể) đang
  bị mất kết nối.


  {% for device in devices %}- ***{{ device }}***

  {% endfor %}

  {% for entity in entities %}  - *{{ entity }}*

  {% endfor %}
visibility:
  - condition: state
    entity: binary_sensor.unavailable_devices
    state: "on"
title: Unavailable Devices
```
