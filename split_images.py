import os
import glob
import re

base = 'C:/Users/xx8897/codespace/profile'
script_path = os.path.join(base, 'js/script.js')

# 1. Split Grafana
with open(os.path.join(base, 'slides/homelab/homelab-monitoring---grafana.html'), 'r', encoding='utf-8') as f:
    grafana_content = f.read()

# Create 4 files
template = """<div class="slide bg-light is-light">
  <div class="slide-inner">
    <div class="content-header">
      <div class="section-label">HOMELAB AI STACK &mdash; MLOPS</div>
      <h2>全棧 MLOps 監控：Grafana Dashboard</h2>
    </div>
    <div class="img-showcase" style="height: 100%;">
      <div class="img-card"><img src="{img_src}" alt="{alt}" style="max-height: 70vh; object-fit: contain;"><div class="img-card-caption">{caption}</div></div>
    </div>
  </div>
  <div class="slide-num"></div>
</div>"""

grafana_slides = [
    ("images/homelab/grafana/grafana_mac_system_resource.png", "Mac 系統資源監控", "Mac M4 系統資源監控 &mdash; CPU / 記憶體 / GPU 使用率"),
    ("images/homelab/grafana/grafana_gpu_monitoring.png", "GPU 監控", "RTX 3070 GPU 監控 &mdash; 溫度 / VRAM / 推理佇列"),
    ("images/homelab/grafana/grafana_docker_container_monitoring.png", "Docker 容器監控", "Docker 容器監控 &mdash; 7 容器統一管理與健康狀態"),
    ("images/homelab/grafana/grafana_litellm_monitoring.png", "LiteLLM 監控", "LiteLLM Proxy 監控 &mdash; API 路由與負載均衡")
]

for i, (img, alt, cap) in enumerate(grafana_slides):
    out = template.format(img_src=img, alt=alt, caption=cap)
    with open(os.path.join(base, f'slides/homelab/homelab-monitoring-grafana-{i+1}.html'), 'w', encoding='utf-8') as f:
        f.write(out)
os.remove(os.path.join(base, 'slides/homelab/homelab-monitoring---grafana.html'))


# 2. Split Network & Alert
network_slides = [
    ("images/homelab/network/tailscale_mesh_vpn.png", "Tailscale VPN", "Tailscale Mesh VPN &mdash; 三機安全互聯"),
    ("images/homelab/network/telegram_bot_alert.png", "Telegram Alert", "Telegram Bot &mdash; 6 組關鍵告警規則即時推送")
]
for i, (img, alt, cap) in enumerate(network_slides):
    out = template.replace('Grafana Dashboard', '網路與告警').format(img_src=img, alt=alt, caption=cap)
    with open(os.path.join(base, f'slides/homelab/homelab-monitoring-network-{i+1}.html'), 'w', encoding='utf-8') as f:
        f.write(out)
os.remove(os.path.join(base, 'slides/homelab/homelab-monitoring---network-and-alert.html'))


# 3. Split ETF
# P16: 16_etf-ai-product---wizard.html -> etf-ai-product---wizard.html
etf_wizard_content = """<div class="slide bg-light is-light">
  <div class="slide-inner" style="padding: 0; display:flex; align-items:center; justify-content:center; height:100%;">
    <img src="images/etf_advisor/etf_wizard_ui.png" alt="ETF Wizard" style="width:100%; height:100%; object-fit:contain;">
  </div>
  <div class="slide-num"></div>
</div>"""
with open(os.path.join(base, 'slides/etf/etf-ai-product---wizard.html'), 'w', encoding='utf-8') as f:
    f.write(etf_wizard_content)

etf_report_content = """<div class="slide bg-light is-light">
  <div class="slide-inner" style="padding: 0; display:flex; align-items:center; justify-content:center; height:100%;">
    <img src="images/etf_advisor/etf_report_ui.png" alt="ETF Report" style="width:100%; height:100%; object-fit:contain;">
  </div>
  <div class="slide-num"></div>
</div>"""
with open(os.path.join(base, 'slides/etf/etf-ai-product---report.html'), 'w', encoding='utf-8') as f:
    f.write(etf_report_content)


# 4. Split Stock Gift Details (P22)
# stock-gift-product---details.html
stock_details_1 = """<div class="slide bg-light is-light">
  <div class="slide-inner" style="padding: 0; display:flex; align-items:center; justify-content:center; height:100%;">
    <img src="images/stock_gift/stock_gift_detail_view_1.png" alt="Stock Detail 1" style="width:100%; height:100%; object-fit:contain;">
  </div>
  <div class="slide-num"></div>
</div>"""
with open(os.path.join(base, 'slides/stock/stock-gift-product-details-1.html'), 'w', encoding='utf-8') as f:
    f.write(stock_details_1)

stock_details_2 = """<div class="slide bg-light is-light">
  <div class="slide-inner" style="padding: 0; display:flex; align-items:center; justify-content:center; height:100%;">
    <img src="images/stock_gift/stock_gift_detail_view_2.png" alt="Stock Detail 2" style="width:100%; height:100%; object-fit:contain;">
  </div>
  <div class="slide-num"></div>
</div>"""
with open(os.path.join(base, 'slides/stock/stock-gift-product-details-2.html'), 'w', encoding='utf-8') as f:
    f.write(stock_details_2)
os.remove(os.path.join(base, 'slides/stock/stock-gift-product---details.html'))


# 5. Split Exhibit (P32)
exhibit_slides = [
    ("images/exhibit/exhibit_homepage.png", "Exhibit 首頁", "Exhibit &mdash; 首頁與精選"),
    ("images/exhibit/exhibit_filter_region.png", "地區篩選", "地區與分類多維度篩選"),
    ("images/exhibit/exhibit_detail.png", "展覽詳情", "展覽詳細資訊與地圖"),
]
for i, (img, alt, cap) in enumerate(exhibit_slides):
    out = template.replace('HOMELAB AI STACK &mdash; MLOPS', 'EXHIBIT &mdash; UI/UX') \
                  .replace('全棧 MLOps 監控：Grafana Dashboard', '展覽平台介面展示').format(img_src=img, alt=alt, caption=cap)
    with open(os.path.join(base, f'slides/misc/exhibit-{i+1}.html'), 'w', encoding='utf-8') as f:
        f.write(out)
os.remove(os.path.join(base, 'slides/misc/exhibit.html'))


# Rewrite script.js
final_order = [
    "slides/cover/cover.html",
    "slides/capabilities/skills.html",
    "slides/homelab/homelab-chapter.html",
    "slides/homelab/homelab-pain-points.html",
    "slides/homelab/05_homelab-design-philosophy-and-architecture.html",
    "slides/homelab/homelab-fallback-and-moe.html",
    "slides/homelab/homelab-monitoring-grafana-1.html",
    "slides/homelab/homelab-monitoring-grafana-2.html",
    "slides/homelab/homelab-monitoring-grafana-3.html",
    "slides/homelab/homelab-monitoring-grafana-4.html",
    "slides/homelab/homelab-monitoring-network-1.html",
    "slides/homelab/homelab-monitoring-network-2.html",
    "slides/misc/hermes-agent.html",
    "slides/homelab/homelab-litellm.html",
    "slides/homelab/homelab-summary.html",
    "slides/etf/etf-ai-chapter.html",
    "slides/etf/etf-ai-pain-points.html",
    "slides/etf/etf-ai-rag-pipeline.html",
    "slides/etf/etf-ai-product---wizard.html",
    "slides/etf/etf-ai-product---report.html",
    "slides/etf/etf-ai-summary.html",
    "slides/stock/stock-gift-chapter.html",
    "slides/stock/stock-gift-pain-points.html",
    "slides/stock/stock-gift-product---homepage.html",
    "slides/stock/stock-gift-product-details-1.html",
    "slides/stock/stock-gift-product-details-2.html",
    "slides/stock/stock-gift-tech---refactor.html",
    "slides/stock/stock-gift-tech---serverless.html",
    "slides/stock/stock-gift-summary.html",
    "slides/misc/synthforge-chapter.html",
    "slides/misc/synthforge-design-philosophy.html",
    "slides/misc/synthforge-rules.html",
    "slides/misc/synthforge-architecture.html",
    "slides/misc/synthforge-visual-tour.html",
    "slides/misc/synthforge-summary.html",
    "slides/misc/exhibit-1.html",
    "slides/misc/exhibit-2.html",
    "slides/misc/exhibit-3.html",
    "slides/experience/33_experience.html",
    "slides/misc/positioning.html",
    "slides/closing/closing.html"
]

script_content = open(script_path, 'r', encoding='utf-8').read()
new_array_str = "const slideFiles = [\n  " + ",\n  ".join(f'"{f}"' for f in final_order) + "\n];"
script_content = re.sub(r'const slideFiles = \[[\s\S]*?\];', new_array_str, script_content)
with open(script_path, 'w', encoding='utf-8') as f:
    f.write(script_content)

print("Split operation complete.")
