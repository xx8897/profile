let currentSlide = 0;
const slides = document.querySelectorAll('.slide');
const totalSlides = slides.length;
const dotsContainer = document.getElementById('navDots');

for (let i = 0; i < totalSlides; i++) {
  const dot = document.createElement('button');
  dot.className = 'nav-dot' + (i === 0 ? ' active' : '');
  dot.onclick = () => goToSlide(i);
  dotsContainer.appendChild(dot);
}

function goToSlide(index) {
  if (index < 0 || index >= totalSlides) return;
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
  if (e.key === 'End') { e.preventDefault(); goToSlide(totalSlides - 1); }
});

let touchStartX = 0;
document.addEventListener('touchstart', (e) => { touchStartX = e.touches[0].clientX; });
document.addEventListener('touchend', (e) => {
  const diff = touchStartX - e.changedTouches[0].clientX;
  if (Math.abs(diff) > 50) { diff > 0 ? nextSlide() : prevSlide(); }
});