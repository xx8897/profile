import os
import re

base = 'C:/Users/xx8897/codespace/profile/slides'

def fix_spacing(filepath):
    if not os.path.exists(filepath): return
    content = open(filepath, 'r', encoding='utf-8').read()
    
    # 1. Remove margin-top from the first element after content-header
    # Look for the first <div> or element after </div> of content-header
    new_content = re.sub(r'(</div>\s+<div[^>]*style="[^"]*)margin-top:\s*\d+px;?\s*', r'\1', content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed spacing in {filepath}")

# List of files identified with margin-top issues after header
files_to_fix = [
    'homelab/homelab-litellm-v2.html',
    'misc/synthforge-visual-tour.html',
    'stock/stock-gift-automation.html',
    'stock/stock-gift-product---homepage.html',
    'homelab/homelab-fallback-and-moe.html',
    'etf/etf-ai-rag-pipeline.html',
    'stock/stock-gift-tech---refactor.html',
    'stock/stock-gift-tech---serverless.html'
]

for f in files_to_fix:
    fix_spacing(os.path.join(base, f))

print("Spacing cleanup complete.")
