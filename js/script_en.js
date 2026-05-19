const portfolioConfig = [
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
      "slides/homelab/homelab-litellm-ui.html",
      "slides/homelab/homelab-litellm-v2.html",
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
      "slides/etf/etf-ai-product---breakdown.html",
      "slides/etf/etf-ai-backend.html",
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
      "slides/stock/stock-gift-product-filter.html",
      "slides/stock/stock-gift-product-5star.html",
      "slides/stock/stock-gift-product-details-2.html",
      "slides/stock/stock-gift-tech---refactor.html",
      "slides/stock/stock-gift-tech---valuation.html",
      "slides/stock/stock-gift-tech---serverless.html",
      "slides/stock/stock-gift-automation.html",
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
      "slides/misc/exhibit-chapter.html",
      "slides/misc/exhibit-1.html",
      "slides/misc/exhibit-2.html",
      "slides/misc/exhibit-tech.html"
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

const slideFiles = portfolioConfig.flatMap(section => section.slides);

let currentSlide = 0;
let slides = [];
let translations = {};

const deck = document.getElementById('deck');
const dotsContainer = document.getElementById('navDots');
const loadingScreen = document.getElementById('loadingScreen');

const translationFiles = [
  'js/translations/introduction.json',
  'js/translations/homelab.json',
  'js/translations/etf.json',
  'js/translations/stock.json',
  'js/translations/synthforge.json',
  'js/translations/exhibit.json',
  'js/translations/experience.json'
];

// 套用翻譯到 raw HTML 字串
function applyTranslationsToHtml(htmlStr) {
  let translated = htmlStr;
  for (const [zh, en] of Object.entries(translations)) {
    translated = translated.split(zh).join(en);
  }
  return translated;
}

async function init() {
  try {
    // 載入多個翻譯 JSON 檔案並合併為單一 translations 物件
    const transResponses = await Promise.all(
      translationFiles.map(file => fetch(file).then(res => {
        if (!res.ok) throw new Error(`Failed to load translation file: ${file}`);
        return res.json();
      }))
    );
    translations = Object.assign({}, ...transResponses);

    // 載入所有投影片
    const slidePromises = slideFiles.map(async (file, index) => {
      const response = await fetch(file);
      if (!response.ok) throw new Error(`Failed to load ${file}`);
      let html = await response.text();
      
      // 在轉換為 DOM 之前，直接替換字串
      html = applyTranslationsToHtml(html);
      
      const tempDiv = document.createElement('div');
      tempDiv.innerHTML = html;

      const slideDiv = tempDiv.querySelector('.slide');
      if (slideDiv) {
        slideDiv.setAttribute('data-index', index);
        const slideNum = slideDiv.querySelector('.slide-num');
        if (slideNum) {
          slideNum.textContent = `${(index + 1).toString().padStart(2, '0')} / ${slideFiles.length.toString().padStart(2, '0')}`;
        }
        return slideDiv;
      }
      return null;
    });

    const loadedSlides = await Promise.all(slidePromises);
    slides = loadedSlides.filter(s => s !== null);

    slides.forEach((slide, i) => {
      deck.appendChild(slide);
      const dot = document.createElement('button');
      dot.className = 'nav-dot' + (i === 0 ? ' active' : '');
      dot.onclick = () => goToSlide(i);
      dotsContainer.appendChild(dot);
    });

    if (slides.length > 0) {
      slides[0].classList.add('active');
    }

    setTimeout(() => {
      loadingScreen.style.opacity = '0';
      setTimeout(() => loadingScreen.style.display = 'none', 500);
    }, 300);

  } catch (error) {
    console.error('Error initializing English portfolio:', error);
    loadingScreen.innerHTML = `<div style="color:white;text-align:center;">Failed to load. Please check your connection.<br>${error.message}</div>`;
  }
}

function goToSlide(index) {
  if (index < 0 || index >= slides.length) return;
  slides[currentSlide].classList.remove('active');
  dotsContainer.children[currentSlide].classList.remove('active');
  currentSlide = index;
  slides[currentSlide].classList.add('active');
  dotsContainer.children[currentSlide].classList.add('active');
  window.scrollTo(0, 0);
}

function nextSlide() { goToSlide(currentSlide + 1); }
function prevSlide() { goToSlide(currentSlide - 1); }

document.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowRight' || e.key === 'ArrowDown') { e.preventDefault(); nextSlide(); }
  if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') { e.preventDefault(); prevSlide(); }
  if (e.key === 'Home') { e.preventDefault(); goToSlide(0); }
  if (e.key === 'End') { e.preventDefault(); goToSlide(slides.length - 1); }
});

let touchStartX = 0;
document.addEventListener('touchstart', (e) => { touchStartX = e.touches[0].clientX; });
document.addEventListener('touchend', (e) => {
  const diff = touchStartX - e.changedTouches[0].clientX;
  if (Math.abs(diff) > 50) { diff > 0 ? nextSlide() : prevSlide(); }
});

init();