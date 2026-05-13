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
      "slides/stock/stock-gift-product-details-2.html",
      "slides/stock/stock-gift-tech---refactor.html",
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
      "slides/misc/exhibit-3.html",
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

// Flatten the config to maintain compatibility with existing logic
const slideFiles = portfolioConfig.flatMap(section => section.slides);


let currentSlide = 0;
let slides = [];
const deck = document.getElementById('deck');
const dotsContainer = document.getElementById('navDots');
const loadingScreen = document.getElementById('loadingScreen');

async function init() {
  try {
    // Load all slides
    const slidePromises = slideFiles.map(async (file, index) => {
      const response = await fetch(file);
      if (!response.ok) throw new Error(`Failed to load ${file}`);
      const html = await response.text();
      const tempDiv = document.createElement('div');
      tempDiv.innerHTML = html;
      
      // Extract the slide div
      const slideDiv = tempDiv.querySelector('.slide');
      if (slideDiv) {
        slideDiv.setAttribute('data-index', index);
        // Ensure index is set correctly for navigation
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

    // Append to deck
    slides.forEach((slide, i) => {
      deck.appendChild(slide);
      
      // Create nav dots
      const dot = document.createElement('button');
      dot.className = 'nav-dot' + (i === 0 ? ' active' : '');
      dot.onclick = () => goToSlide(i);
      dotsContainer.appendChild(dot);
    });

    // Initialize first slide
    if (slides.length > 0) {
      slides[0].classList.add('active');
    }

    // Hide loading screen
    setTimeout(() => {
      loadingScreen.style.opacity = '0';
      setTimeout(() => loadingScreen.style.display = 'none', 500);
    }, 300);

  } catch (error) {
    console.error('Error initializing portfolio:', error);
    loadingScreen.innerHTML = `<div style="color:white;text-align:center;">載入失敗，請檢查網路連線或編碼。<br>${error.message}</div>`;
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
  
  // Update hash if needed
  // window.location.hash = `slide-${index + 1}`;
}

function nextSlide() { goToSlide(currentSlide + 1); }
function prevSlide() { goToSlide(currentSlide - 1); }

// Event Listeners
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

// Start initialization
init();