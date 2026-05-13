import os
import re

base = 'C:/Users/xx8897/codespace/profile'

hooks = {
    'slides/homelab/homelab-chapter.html': {
        'tw': '我把三台電腦串在一起，讓 AI 永遠不會斷線',
        'en': 'I chained three computers together so my AI never goes offline.'
    },
    'slides/etf/etf-ai-chapter.html': {
        'tw': '買 ETF 不是選一檔——讓 AI 根據你的風格配一整組',
        'en': 'Don\'t just pick one ETF—let AI build a portfolio tailored to your style.'
    },
    'slides/stock/stock-gift-chapter.html': {
        'tw': '從自動爬蟲到 DFS 演算法——精準估算數百檔紀念品真實價值',
        'en': 'From web scraping to DFS algorithms: Automatically valuing hundreds of shareholder gifts.'
    },
    'slides/misc/synthforge-chapter.html': {
        'tw': '我寫了 23 條規則與自動化 SOP，打造出絕不失控的超級實習生',
        'en': 'I wrote 23 rules and automated workflows to build an AI intern that never goes rogue.'
    },
    'slides/misc/exhibit-1.html': { 
        # Wait, exhibit doesn't have a chapter.html right now?
        # Oh! In script.js, exhibit just starts with exhibit-1.html.
        # I need to create a chapter slide for Exhibit!
    }
}

template_hook = """
    <!-- User Story Hook -->
    <div style="margin-top: 40px; padding: 20px 30px; background: rgba(255,255,255,0.05); border-left: 4px solid var(--accent); border-radius: 0 12px 12px 0;">
      <div style="font-size: 24px; font-weight: 800; color: #fff; margin-bottom: 8px;">「{tw}」</div>
      <div style="font-size: 15px; color: rgba(255,255,255,0.6); font-style: italic;">"{en}"</div>
    </div>
"""

for file_path, hook in hooks.items():
    if 'exhibit' in file_path: continue
    
    full_path = os.path.join(base, file_path)
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "User Story Hook" not in content:
        # Inject right after <div class="slide-subtitle"...></div>
        hook_html = template_hook.format(tw=hook['tw'], en=hook['en'])
        content = re.sub(r'(<div class="slide-subtitle"[^>]*>.*?</div>)', r'\1' + hook_html, content, flags=re.DOTALL)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)

print("Hooks injected.")
