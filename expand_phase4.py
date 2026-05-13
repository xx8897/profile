import os
import re

base = 'C:/Users/xx8897/codespace/profile'
script_path = os.path.join(base, 'js/script.js')

template = """<div class="slide bg-dark-grid">
  <div class="slide-inner" style="max-width:1000px; padding:60px;">
    <div class="content-header">
      <div class="section-label" style="color:var(--accent);">{subtitle}</div>
      <h2 style="color:#fff;">{title}</h2>
    </div>
    {content}
  </div>
  <div class="slide-num"></div>
</div>"""

# 1. Exhibit Tech
exhibit_content = """
<div style="display:grid; grid-template-columns:1fr 1fr; gap:40px; margin-top:30px;">
  <div>
    <h3 style="color:var(--accent); margin-bottom:16px;">前端架構與 UI 實現</h3>
    <ul style="color:#fff; line-height:2; font-size:16px; padding-left:20px;">
      <li><strong>React 18 + TypeScript</strong><br><span style="color:rgba(255,255,255,0.6);font-size:14px;">嚴謹的型別系統，確保資料流與狀態管理的穩定性</span></li>
      <li><strong>Tailwind CSS + Glassmorphism</strong><br><span style="color:rgba(255,255,255,0.6);font-size:14px;">高度客製化的毛玻璃特效，打造現代化且通透的視覺體驗</span></li>
      <li><strong>Responsive Design (RWD)</strong><br><span style="color:rgba(255,255,255,0.6);font-size:14px;">從手機到桌面端，提供一致流暢的多維度篩選介面</span></li>
    </ul>
  </div>
  <div>
    <h3 style="color:var(--accent); margin-bottom:16px;">AI 與資料層</h3>
    <ul style="color:#fff; line-height:2; font-size:16px; padding-left:20px;">
      <li><strong>資料彙總與清洗</strong><br><span style="color:rgba(255,255,255,0.6);font-size:14px;">從多個不規則的展覽資料源爬取原始資訊並標準化</span></li>
      <li><strong>AI 智慧分類引擎</strong><br><span style="color:rgba(255,255,255,0.6);font-size:14px;">透過大語言模型對展覽內容進行自然語言理解與自動標籤化</span></li>
      <li><strong>多維度動態篩選</strong><br><span style="color:rgba(255,255,255,0.6);font-size:14px;">支援地區、類別、時間的複合式查詢，瞬間定位目標展覽</span></li>
    </ul>
  </div>
</div>
"""
out1 = template.format(subtitle="EXHIBIT &mdash; TECH STACK", title="技術深度：從資料清洗到毛玻璃 UI", content=exhibit_content)
with open(os.path.join(base, 'slides/misc/exhibit-tech.html'), 'w', encoding='utf-8') as f:
    f.write(out1)

# 2. ETF Backend
etf_content = """
<div style="display:flex; flex-direction:column; gap:30px; margin-top:30px;">
  <div style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); padding:24px; border-radius:12px;">
    <h3 style="color:var(--accent); margin-bottom:12px; font-size:20px;">🚀 Dart Frog 微服務後端</h3>
    <div style="color:rgba(255,255,255,0.7); line-height:1.7; font-size:15px;">
      拋棄了傳統 Python 框架，大膽採用 Dart Frog 構建後端，實現了從 Flutter 前端到後端的<b>全棧 Dart 開發體驗</b>。這大幅降低了資料模型 (Models) 的轉換成本，讓端到端的型別安全 (Type Safety) 得以貫徹。
    </div>
  </div>
  
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:20px;">
    <div style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); padding:24px; border-radius:12px;">
      <h3 style="color:var(--accent); margin-bottom:12px; font-size:18px;">🧠 檢索增強生成 (RAG) 管線</h3>
      <div style="color:rgba(255,255,255,0.7); line-height:1.7; font-size:14px;">
        1. 使用 <b>ChromaDB</b> 作為本地向量資料庫。<br>
        2. 動態將使用者的「投資 DNA」轉為 Query 進行相似度檢索。<br>
        3. 將檢索出的 ETF 因子與使用者偏好餵給 <b>GPT-4o</b> 進行推理。<br>
        4. <b>後端防禦性處理層</b>：對 AI 生成的 JSON 進行嚴格清洗與結構驗證。
      </div>
    </div>
    <div style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); padding:24px; border-radius:12px;">
      <h3 style="color:var(--accent); margin-bottom:12px; font-size:18px;">單一事實來源 (SSOT)</h3>
      <div style="color:rgba(255,255,255,0.7); line-height:1.7; font-size:14px;">
        在歷經網頁爬蟲與各類不穩定的 OpenAPI 探勘後，架構最終收斂至<b>使用者提供的單一 Excel 作為知識庫</b>。這消除了外部 API 不穩定的技術風險，讓系統在封閉環境下依然能提供高品質的量化分析。
      </div>
    </div>
  </div>
</div>
"""
out2 = template.format(subtitle="ETF AI ADVISOR &mdash; BACKEND ARCHITECTURE", title="技術深度：Dart 微服務與 RAG 管線", content=etf_content)
with open(os.path.join(base, 'slides/etf/etf-ai-backend.html'), 'w', encoding='utf-8') as f:
    f.write(out2)

# 3. Stock Gift Automation
stock_content = """
<div style="margin-top:30px;">
  <div style="display:flex; align-items:center; gap:30px; margin-bottom:30px;">
    <div style="flex:1;">
      <h3 style="color:var(--accent); margin-bottom:12px; font-size:20px;">⚙️ GitHub Actions 零成本自動化</h3>
      <div style="color:rgba(255,255,255,0.7); line-height:1.7; font-size:15px;">
        利用 GitHub Actions 的排程功能 (Cron Jobs)，每週自動執行 <b>Python 爬蟲腳本</b>，呼叫 FinMind API 抓取台股最新股價。實現了完全 Serverless、零營運成本的即時數據管線。
      </div>
    </div>
    <div style="flex:1;">
      <h3 style="color:var(--accent); margin-bottom:12px; font-size:20px;">☁️ Supabase 雲端資料同步</h3>
      <div style="color:rgba(255,255,255,0.7); line-height:1.7; font-size:15px;">
        將計算完畢的新鮮數據（價格、CP 值、推薦分數）透過 API 直寫 Supabase 雲端資料庫。前端採用即時訂閱，確保使用者看到的永遠是最新資訊，並透過 OAuth 2.0 實現跨裝置持股追蹤。
      </div>
    </div>
  </div>

  <div style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); padding:24px; border-radius:12px;">
    <h3 style="color:var(--accent); margin-bottom:12px; font-size:18px;">🧠 知識與邏輯解耦：V5 DFS 估值引擎</h3>
    <pre style="background:rgba(0,0,0,0.3); padding:16px; border-radius:8px; color:rgba(255,255,255,0.8); font-size:14px; line-height:1.6; margin-bottom:12px;">gift_tree/tree.json   ← 「大腦」可視化 JSON 分類規則樹
         │            (DFS 深度優先搜尋 + 屬性繼承)
         ▼
valuation_v5.py       ← 「執行器」通用演算法引擎，產出最終 CP 值</pre>
    <div style="color:rgba(255,255,255,0.7); font-size:14px; line-height:1.6;">
      將「紀念品值多少錢的規則」抽離成 JSON 樹狀結構，主程式只負責跑 DFS 演算法。非工程師也能透過 Web 介面動態調整估值邏輯，一鍵重算 800+ 支股票，<b>無需修改任何一行 Python 程式碼</b>。
    </div>
  </div>
</div>
"""
out3 = template.format(subtitle="TW STOCK GIFT &mdash; AUTOMATION", title="技術深度：ETL 自動化與 DFS 估值引擎", content=stock_content)
with open(os.path.join(base, 'slides/stock/stock-gift-automation.html'), 'w', encoding='utf-8') as f:
    f.write(out3)

# Update script.js config
script_content = open(script_path, 'r', encoding='utf-8').read()

script_content = script_content.replace(
    '"slides/misc/exhibit-3.html"',
    '"slides/misc/exhibit-3.html",\n      "slides/misc/exhibit-tech.html"'
)

script_content = script_content.replace(
    '"slides/etf/etf-ai-summary.html"',
    '"slides/etf/etf-ai-backend.html",\n      "slides/etf/etf-ai-summary.html"'
)

script_content = script_content.replace(
    '"slides/stock/stock-gift-summary.html"',
    '"slides/stock/stock-gift-automation.html",\n      "slides/stock/stock-gift-summary.html"'
)

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(script_content)

print("Phase 4 expansion slides created and linked.")
