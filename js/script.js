const slideFiles = [
  "slides/cover/01_cover.html",
  "slides/capabilities/02_skills.html",
  "slides/homelab/03_homelab-chapter.html",
  "slides/homelab/04_homelab-pain-points.html",
  "slides/homelab/05_homelab-design-philosophy.html",
  "slides/homelab/06_homelab-architecture.html",
  "slides/homelab/07_homelab-fallback-and-moe.html",
  "slides/homelab/08_homelab-monitoring---grafana.html",
  "slides/homelab/09_homelab-monitoring---network-and-alert.html",
  "slides/misc/10_hermes-agent.html",
  "slides/homelab/11_homelab-litellm.html",
  "slides/homelab/12_homelab-summary.html",
  "slides/etf/13_etf-ai-chapter.html",
  "slides/etf/14_etf-ai-pain-points.html",
  "slides/etf/15_etf-ai-rag-pipeline.html",
  "slides/etf/16_etf-ai-product---wizard.html",
  "slides/etf/17_etf-ai-product---report.html",
  "slides/etf/18_etf-ai-summary.html",
  "slides/stock/19_stock-gift-chapter.html",
  "slides/stock/20_stock-gift-pain-points.html",
  "slides/stock/21_stock-gift-product---homepage.html",
  "slides/stock/22_stock-gift-product---details.html",
  "slides/stock/23_stock-gift-tech---refactor.html",
  "slides/stock/24_stock-gift-tech---serverless.html",
  "slides/stock/25_stock-gift-summary.html",
  "slides/misc/26_synthforge-chapter.html",
  "slides/misc/27_synthforge-design-philosophy.html",
  "slides/misc/28_synthforge-rules.html",
  "slides/misc/29_synthforge-architecture.html",
  "slides/misc/30_synthforge-visual-tour.html",
  "slides/misc/31_synthforge-summary.html",
  "slides/misc/32_exhibit.html",
  "slides/experience/33_experience---work.html",
  "slides/experience/34_experience---education.html",
  "slides/misc/36_key-metrics.html",
  "slides/misc/37_positioning.html",
  "slides/misc/38_tech-stack-overview.html",
  "slides/closing/39_closing.html"
];

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