import os
import glob
import re

base = 'C:/Users/xx8897/codespace/profile'
script_path = os.path.join(base, 'js/script.js')

html_files = glob.glob(os.path.join(base, 'slides', '**', '*.html'), recursive=True)
mappings = {}

for f in html_files:
    d, n = os.path.split(f)
    m = re.match(r'^\d+_(.*)', n)
    if m:
        new_n = m.group(1)
        os.rename(f, os.path.join(d, new_n))
        mappings[n] = new_n
        print('Renamed', n, 'to', new_n)

content = open(script_path, 'r', encoding='utf-8').read()
for old, new in mappings.items():
    content = content.replace(old, new)

open(script_path, 'w', encoding='utf-8').write(content)
print("Updated script.js")
