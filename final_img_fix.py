import os

base = 'C:/Users/xx8897/codespace/profile'

def fix_img(filepath, old_src, new_src):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath}, does not exist.")
        return
    content = open(filepath, 'r', encoding='utf-8').read()
    if old_src in content:
        content = content.replace(old_src, new_src)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filepath}: {old_src} -> {new_src}")

# HomeLab
fix_img(os.path.join(base, 'slides/homelab/homelab-monitoring-network-1.html'), 
        'images/homelab/network/tailscale_mesh_vpn.png', 
        'images/homelab/grafana/grafana_tailscale_network.png')
fix_img(os.path.join(base, 'slides/homelab/homelab-monitoring-network-2.html'), 
        'images/homelab/network/telegram_bot_alert.png', 
        'images/homelab/hermes/telegram_alert_bot_demo.png')

# ETF
fix_img(os.path.join(base, 'slides/etf/etf-ai-product---wizard.html'), 
        'images/etf_advisor/etf_wizard_ui.png', 
        'images/etf/etf_wizard_step1_risk_profile.png')
fix_img(os.path.join(base, 'slides/etf/etf-ai-product---report.html'), 
        'images/etf_advisor/etf_report_ui.png', 
        'images/etf/etf_report_portfolio_recommendation.png')

# Stock Gift
fix_img(os.path.join(base, 'slides/stock/stock-gift-product-details-1.html'), 
        'images/stock_gift/stock_gift_detail_view_1.png', 
        'images/stock/twstock_table_owned_gifts_guide.png')
fix_img(os.path.join(base, 'slides/stock/stock-gift-product-details-2.html'), 
        'images/stock_gift/stock_gift_detail_view_2.png', 
        'images/stock/twstock_gift_tree_readme_editor.png')

# Exhibit
fix_img(os.path.join(base, 'slides/misc/exhibit-1.html'), 
        'images/exhibit/exhibit_homepage.png', 
        'images/exhibit/exhibit_homepage_hero_carousel.png')
fix_img(os.path.join(base, 'slides/misc/exhibit-2.html'), 
        'images/exhibit/exhibit_filter_region.png', 
        'images/exhibit/exhibit_detail_page_ai_category.png')
fix_img(os.path.join(base, 'slides/misc/exhibit-3.html'), 
        'images/exhibit/exhibit_detail.png', 
        'images/exhibit/exhibit_detail_page_map_section.png')

print("Final path fix applied.")
