/* start searchBtn function */
let searchBtn = document.querySelector('#search-btn');
let searchBar = document.querySelector('.search-bar-container');

/* adminForm */
let adminBtn = document.querySelector('#admin-btn');
let adminForm = document.querySelector('.admin-form-container');
let adminClose = document.querySelector('#admin-close');

/* loginForm */
let loginFormContainer = document.querySelector('.login-form-container');
let formCloseIcon = document.getElementById('form-close');

/*navbar*/
let menu = document.querySelector('#menu-bar');
let navbar = document.querySelector('.navbar');

/* video */
let videoBtn = document.querySelectorAll('.vid-btn');

/*searchBtn */
window.onscroll = () =>{
    searchBtn.classList.remove('fa-times');
    searchBar.classList.remove('active');
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');
    loginFormContainer.classList.remove('active'); 
    adminForm.classList.remove('active');
};

// Show login form when the document is loaded
document.addEventListener('DOMContentLoaded', function () {
    showLoginForm();
});

searchBtn.addEventListener('click', () =>{
    searchBtn.classList.toggle('fa-times');
    searchBar.classList.toggle('active');
});

/* navbar */
menu.addEventListener('click', () =>{
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
});

/* admin form */
if (adminBtn) {
    adminBtn.addEventListener('click', () => {
        adminForm.classList.add('active');
    });
}

if (adminClose) {
    adminClose.addEventListener('click', () => {
        adminForm.classList.remove('active');
    });
}

// Function to show the login form container
function showLoginForm() {
    loginFormContainer.classList.add('active');
}

// Hide login form when close icon is clicked
if (formCloseIcon) {
    formCloseIcon.addEventListener('click', () => {
        loginFormContainer.classList.remove('active');
    });
}

videoBtn.forEach(btn =>{
    btn.addEventListener('click', ()=>{
        document.querySelector('.controls .active').classList.remove('active');
        btn.classList.add('active');
        let src = btn.getAttribute('data-src');
        document.querySelector('#video-slider').src = src;
    });
});
