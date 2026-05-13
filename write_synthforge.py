import os

base = 'C:/Users/xx8897/codespace/profile'

template = """<div class="slide bg-dark-grid">
  <div class="slide-inner" style="max-width:1000px; padding:60px;">
    <div class="content-header">
      <div class="section-label" style="color:var(--accent);">SYNTHFORGE &mdash; {subtitle}</div>
      <h2 style="color:#fff;">{title}</h2>
    </div>
    {content}
  </div>
  <div class="slide-num"></div>
</div>"""

# 1. Design Philosophy
philosophy_content = """
<div style="display:flex; flex-direction:column; gap:20px; margin-top:30px;">
  <div class="summary-card" style="padding:24px; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1);">
    <div style="font-size:20px; font-weight:800; color:#fff; margin-bottom:8px;">1. Automation First / 自動化優先</div>
    <div style="color:rgba(255,255,255,0.6); line-height:1.6;">Automate repetitive tasks to focus on architectural decisions.</div>
  </div>
  <div class="summary-card" style="padding:24px; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1);">
    <div style="font-size:20px; font-weight:800; color:#fff; margin-bottom:8px;">2. Test-Driven Development / 測試驅動開發</div>
    <div style="color:rgba(255,255,255,0.6); line-height:1.6;">Write tests first to ensure AI-generated code meets specifications.</div>
  </div>
  <div class="summary-card" style="padding:24px; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1);">
    <div style="font-size:20px; font-weight:800; color:#fff; margin-bottom:8px;">3. Security by Default / 預設安全</div>
    <div style="color:rgba(255,255,255,0.6); line-height:1.6;">Built-in security checks running continuously in the background.</div>
  </div>
  <div class="summary-card" style="padding:24px; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1);">
    <div style="font-size:20px; font-weight:800; color:#fff; margin-bottom:8px;">4. Documentation as Code / 文件即代碼</div>
    <div style="color:rgba(255,255,255,0.6); line-height:1.6;">Keep docs in sync automatically with code changes.</div>
  </div>
</div>
"""
out1 = template.format(subtitle="DESIGN PHILOSOPHY", title="核心原則 (Core Principles)", content=philosophy_content)
with open(os.path.join(base, 'slides/misc/synthforge-design-philosophy.html'), 'w', encoding='utf-8') as f:
    f.write(out1)


# 2. Architecture
architecture_content = """
<div style="display:grid; grid-template-columns:1fr 1fr; gap:40px; margin-top:30px;">
  <div>
    <h3 style="color:var(--accent); margin-bottom:16px;">Key Features</h3>
    <ul style="color:#fff; line-height:2; font-size:16px; padding-left:20px;">
      <li><strong>🤖 4 Specialized AI Agents</strong><br><span style="color:rgba(255,255,255,0.6);font-size:14px;">Planner, Executor, Reviewer, Self-Improvement</span></li>
      <li><strong>⚡ Automated Workflows</strong><br><span style="color:rgba(255,255,255,0.6);font-size:14px;">TDD, Feature Dev, Bug Fixing, Refactoring</span></li>
      <li><strong>🔧 Unified CLI</strong><br><span style="color:rgba(255,255,255,0.6);font-size:14px;">One command for all operations</span></li>
      <li><strong>📋 23 Governance Rules</strong><br><span style="color:rgba(255,255,255,0.6);font-size:14px;">Strict constraints to ensure code quality</span></li>
    </ul>
  </div>
  <div>
    <h3 style="color:var(--accent); margin-bottom:16px;">System Structure</h3>
    <pre style="background:rgba(0,0,0,0.3); padding:20px; border-radius:8px; color:rgba(255,255,255,0.8); font-size:13px; line-height:1.5;">
synthforge/
├── 📄 VIBE_GUIDE.md     ← AI entry point
├── 📁 rules/            ← 23 governance rules
├── 📁 devtools/         ← CLI & analyzers
├── 📁 workflows/        ← Automation engine
├── 📁 agents/           ← Specialized AI
├── 📁 skills/           ← Reusable tools
└── 📁 core_lib/         ← Infrastructure
    </pre>
  </div>
</div>
"""
out2 = template.format(subtitle="ARCHITECTURE", title="系統架構與功能總覽", content=architecture_content)
with open(os.path.join(base, 'slides/misc/synthforge-architecture.html'), 'w', encoding='utf-8') as f:
    f.write(out2)


# 3. Visual Tour -> Decision Tree / Mission Control
visual_tour_content = """
<div style="margin-top:30px;">
  <div style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); padding:30px; border-radius:12px;">
    <h3 style="color:var(--accent); margin-bottom:20px;">AI Agent Decision Tree (VIBE_GUIDE.md)</h3>
    <pre style="color:#fff; font-family:monospace; font-size:15px; line-height:1.8;">
START: Read VIBE_GUIDE.md
  ↓
QUESTION: What is your task?
  ↓
  ├─ "Start new feature"
  │   → Read: GIT_WORKFLOW.md
  │   → Use: CLI workflow run feature_development.yml
  │
  ├─ "Fix a bug"
  │   → Use: CLI workflow run bug_fix.yml
  │
  ├─ "Git operations"
  │   → Use: CLI git commit/push/pr
  │
  └─ "Check Status"
      → Read: ROADMAP_v2.md
    </pre>
  </div>
</div>
"""
out3 = template.format(subtitle="VIBE GUIDE", title="AI 代理決策樹 (Decision Tree)", content=visual_tour_content)
with open(os.path.join(base, 'slides/misc/synthforge-visual-tour.html'), 'w', encoding='utf-8') as f:
    f.write(out3)

print("Synthforge text restoration complete.")
