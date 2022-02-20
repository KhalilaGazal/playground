const toggle = document.querySelector('.nav-toggle-btn');
const nav1 = document.querySelector('.secondary-nav');
const nav2 = document.querySelector('.tertiary-nav');

toggle.addEventListener('click', () => {
  nav1.classList.toggle('nav-visible');
  nav2.classList.toggle('nav-visible');
});