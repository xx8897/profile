import os
import glob

base = 'C:/Users/xx8897/codespace/profile'

def fix_layout(filepath, section_label, title, img_src, alt):
    content = f"""<div class="slide bg-light is-light">
  <div class="slide-inner" style="height: 100%; display: flex; flex-direction: column;">
    <div class="content-header" style="flex-shrink: 0;">
      <div class="section-label">{section_label}</div>
      <h2>{title}</h2>
    </div>
    <div style="flex: 1; min-height: 0; display: flex; align-items: center; justify-content: center; overflow: hidden; padding-bottom: 20px;">
      <img src="{img_src}" alt="{alt}" style="max-width: 100%; max-height: 100%; object-fit: contain; border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
    </div>
  </div>
  <div class="slide-num"></div>
</div>"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


# Grafana
grafana = [
    ("homelab-monitoring-grafana-1.html", "images/homelab/grafana/grafana_mac_system_resource.png", "Mac 系統資源監控 &mdash; CPU / 記憶體 / GPU 使用率"),
    ("homelab-monitoring-grafana-2.html", "images/homelab/grafana/grafana_gpu_monitoring.png", "RTX 3070 GPU 監控 &mdash; 溫度 / VRAM / 推理佇列"),
    ("homelab-monitoring-grafana-3.html", "images/homelab/grafana/grafana_docker_container_monitoring.png", "Docker 容器監控 &mdash; 7 容器統一管理與健康狀態"),
    ("homelab-monitoring-grafana-4.html", "images/homelab/grafana/grafana_litellm_monitoring.png", "LiteLLM Proxy 監控 &mdash; API 路由與負載均衡")
]
for f, img, alt in grafana:
    fix_layout(os.path.join(base, 'slides/homelab', f), "HOMELAB AI STACK &mdash; MLOPS", "全棧 MLOps 監控：Grafana Dashboard", img, alt)


# Network
network = [
    ("homelab-monitoring-network-1.html", "images/homelab/network/tailscale_mesh_vpn.png", "Tailscale Mesh VPN &mdash; 三機安全互聯"),
    ("homelab-monitoring-network-2.html", "images/homelab/network/telegram_bot_alert.png", "Telegram Bot &mdash; 6 組關鍵告警規則即時推送")
]
for f, img, alt in network:
    fix_layout(os.path.join(base, 'slides/homelab', f), "HOMELAB AI STACK &mdash; MLOPS", "網路與告警", img, alt)

# Exhibit
exhibit = [
    ("exhibit-1.html", "images/exhibit/exhibit_homepage.png", "Exhibit &mdash; 首頁與精選"),
    ("exhibit-2.html", "images/exhibit/exhibit_filter_region.png", "地區與分類多維度篩選"),
    ("exhibit-3.html", "images/exhibit/exhibit_detail.png", "展覽詳細資訊與地圖"),
]
for f, img, alt in exhibit:
    fix_layout(os.path.join(base, 'slides/misc', f), "EXHIBIT &mdash; UI/UX", "展覽平台介面展示", img, alt)

print("Layout fix applied.")
