 // DOM elements
 const burgerIcon = document.getElementById('burger-icon');
 const sideNav = document.getElementById('side-nav');
 const overlay = document.getElementById('overlay');
 const feedContainer = document.getElementById('feed-container');
 
 // Toggle side navigation
 function toggleSideNav() {
     burgerIcon.classList.toggle('active');
     sideNav.classList.toggle('open');
     overlay.classList.toggle('active');
 }
 
 // Event listeners
 burgerIcon.addEventListener('click', toggleSideNav);
 overlay.addEventListener('click', toggleSideNav);