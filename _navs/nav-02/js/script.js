const toggle = document.querySelector('.nav-toggle-btn');
const nav = document.querySelector('.secondary-nav');

toggle.addEventListener('click', () => {
  nav.classList.toggle('nav-visible');
});