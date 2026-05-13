import os
import re

script_path = 'C:/Users/xx8897/codespace/profile/js/script.js'

with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the array with portfolioConfig
new_config = """const portfolioConfig = [
  {
    section: "Introduction",
    slides: [
      "slides/cover/cover.html",
      "slides/capabilities/skills.html"
    ]
  },
  {
    section: "HomeLab AI Stack",
    slides: [
      "slides/homelab/homelab-chapter.html",
      "slides/homelab/homelab-pain-points.html",
      "slides/homelab/homelab-design-philosophy-and-architecture.html",
      "slides/homelab/homelab-fallback-and-moe.html",
      "slides/homelab/homelab-monitoring-grafana-1.html",
      "slides/homelab/homelab-monitoring-grafana-2.html",
      "slides/homelab/homelab-monitoring-grafana-3.html",
      "slides/homelab/homelab-monitoring-grafana-4.html",
      "slides/homelab/homelab-monitoring-network-1.html",
      "slides/homelab/homelab-monitoring-network-2.html",
      "slides/misc/hermes-agent.html",
      "slides/homelab/homelab-litellm.html",
      "slides/homelab/homelab-summary.html"
    ]
  },
  {
    section: "ETF AI Advisor",
    slides: [
      "slides/etf/etf-ai-chapter.html",
      "slides/etf/etf-ai-pain-points.html",
      "slides/etf/etf-ai-rag-pipeline.html",
      "slides/etf/etf-ai-product---wizard.html",
      "slides/etf/etf-ai-product---report.html",
      "slides/etf/etf-ai-summary.html"
    ]
  },
  {
    section: "TW Stock Gift",
    slides: [
      "slides/stock/stock-gift-chapter.html",
      "slides/stock/stock-gift-pain-points.html",
      "slides/stock/stock-gift-product---homepage.html",
      "slides/stock/stock-gift-product-details-1.html",
      "slides/stock/stock-gift-product-details-2.html",
      "slides/stock/stock-gift-tech---refactor.html",
      "slides/stock/stock-gift-tech---serverless.html",
      "slides/stock/stock-gift-summary.html"
    ]
  },
  {
    section: "SynthForge",
    slides: [
      "slides/misc/synthforge-chapter.html",
      "slides/misc/synthforge-design-philosophy.html",
      "slides/misc/synthforge-rules.html",
      "slides/misc/synthforge-architecture.html",
      "slides/misc/synthforge-visual-tour.html",
      "slides/misc/synthforge-summary.html"
    ]
  },
  {
    section: "Exhibit UI/UX",
    slides: [
      "slides/misc/exhibit-1.html",
      "slides/misc/exhibit-2.html",
      "slides/misc/exhibit-3.html"
    ]
  },
  {
    section: "Experience & Closing",
    slides: [
      "slides/experience/experience.html",
      "slides/misc/positioning.html",
      "slides/closing/closing.html"
    ]
  }
];

// Flatten the config to maintain compatibility with existing logic
const slideFiles = portfolioConfig.flatMap(section => section.slides);
"""

# Replace the `const slideFiles = [ ... ];` block
content = re.sub(r'const slideFiles = \[[\s\S]*?\];', new_config, content)

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Config updated!")
