import os
import re

def split_slides():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Create slides directory
    os.makedirs('slides', exist_ok=True)

    # Slide patterns
    # Slides are marked like: <!-- ===== SLIDE X: NAME ===== -->
    # <div class="slide ..."> ... </div>
    
    # We want to group slides by category
    # Categories seen in index.html:
    # 1. COVER
    # 2. SKILLS (CAPABILITIES)
    # 3. HOMELAB (SLIDE 3-11)
    # 4. ETF (SLIDE 12-20?) - Need to check
    # Let's just split them by slide number and name first.
    
    slides_matches = re.findall(r'(<!-- ===== SLIDE (\d+): (.*?) ===== -->\s*<div class="slide.*?data-index="(\d+)".*?>(.*?)</div>\s*</div>)', content, re.DOTALL)
    
    print(f"Found {len(slides_matches)} slides matches using regex.")
    
    # Actually, the slides might have nested div, so regex for </div> might be tricky.
    # Let's use a more robust way: find <!-- ===== SLIDE X: ... ===== --> as markers.
    
    markers = list(re.finditer(r'<!-- ===== SLIDE (\d+): (.*?) ===== -->', content))
    
    for i in range(len(markers)):
        start_idx = markers[i].start()
        end_idx = markers[i+1].start() if i+1 < len(markers) else content.find('</div><!-- end slide-deck -->')
        
        slide_block = content[start_idx:end_idx].strip()
        
        slide_num = markers[i].group(1)
        slide_name = markers[i].group(2).lower().replace(' ', '-').replace('&', 'and').strip()
        
        # Determine category based on name or number
        category = "misc"
        if "cover" in slide_name: category = "cover"
        elif "skills" in slide_name or "capabilities" in slide_name: category = "capabilities"
        elif "homelab" in slide_name: category = "homelab"
        elif "etf" in slide_name: category = "etf"
        elif "stock" in slide_name: category = "stock"
        elif "experience" in slide_name or "education" in slide_name or "work" in slide_name: category = "experience"
        elif "closing" in slide_name: category = "closing"
        elif "tech stack" in slide_name: category = "closing"
        
        os.makedirs(f'slides/{category}', exist_ok=True)
        filename = f'slides/{category}/{slide_num.zfill(2)}_{slide_name}.html'
        
        # Clean up the block: remove the marker comment and the outer data-index div wrapping if we want, 
        # but the current logic seems to need the .slide div.
        
        with open(filename, 'w', encoding='utf-8') as sf:
            sf.write(slide_block)
        print(f"Saved {filename}")

if __name__ == "__main__":
    split_slides()
