const toggle = document.querySelector('.nav-toggle-btn');
const nav = document.querySelector('.nav-secondary');

toggle.addEventListener('click', () => {
  nav.classList.toggle('nav-visible');
});