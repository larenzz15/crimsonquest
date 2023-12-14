/* start searchBtn function */
let searchBtn = document.querySelector('#search-btn');
let searchBar = document.querySelector('.search-bar-container');

/* adminForm */
let adminBtn = document.querySelector('#admin-btn');
let adminForm = document.querySelector('.admin-form-container');
let adminClose = document.querySelector('#admin-close');

/* loginForm 
let formBtn = document.querySelector('.btn');
let loginForm = document.querySelector('.login-form-container');
let formClose = document.querySelector('#form-close'); 
*/

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
    loginForm.classList.remove('active'); 
    adminForm.classList.remove('active');
}

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


/*login form
formBtn.addEventListener('click', () =>{
    loginForm.classList.add('active');
});

formClose.addEventListener('click', () =>{
    loginForm.classList.remove('active');
}); 
*/

/*
document.getElementById("exploreBtn").addEventListener("click", function (e) {
    e.preventDefault(); // Prevent the default behavior of the anchor link
    document.getElementById("login-form-container").classList.add("active");
});

document.getElementById("form-close").addEventListener("click", function () {
    document.getElementById("login-form-container").classList.remove("active");
});
*/

// user login
document.addEventListener("DOMContentLoaded", function () {
    const exploreBtn = document.getElementById("exploreBtn");
    const showLoginFormLink = document.getElementById("showLoginForm");
    const showRegisterFormLink = document.getElementById("showRegisterForm");
    const loginFormContainer = document.querySelector(".login-form-container");
    const registerFormContainer = document.querySelector(".register-form-container");
    const formCloseIcon = document.getElementById("form-close");
    const registerCloseIcon = document.getElementById("register-close");

    // Function to show the login form container
    function showLoginForm() {
        loginFormContainer.classList.add("active");
    }

    // Function to hide the login form container
    function hideLoginForm() {
        loginFormContainer.classList.remove("active");
    }

    function showRegisterForm() {
        registerFormContainer.classList.add("active");
    }

    // Function to hide the register form container
    function hideRegisterForm() {
        registerFormContainer.classList.remove("active");
    }

    // Show login form when Explore button is clicked
    exploreBtn.addEventListener("click", function (e) {
        e.preventDefault();
        showLoginForm();
    });

    // Show register form when "Register Now" is clicked
    showRegisterFormLink.addEventListener("click", function (e) {
        e.preventDefault();
        showRegisterForm();
        hideLoginForm(); // Make sure to hide the login form when showing the register form.
    });

    // Show login form when "Login Now" is clicked
    showLoginFormLink.addEventListener("click", function (e) {
        e.preventDefault();
        showLoginForm();
        hideRegisterForm(); // Make sure to hide the register form when showing the login form.
    });

    // Hide login form when close icon is clicked
    formCloseIcon.addEventListener("click", function () {
        hideLoginForm();
    });

    // Hide register form when close icon is clicked
    registerCloseIcon.addEventListener("click", function () {
        hideRegisterForm();
    });

    

});
// user login end

// register acc 




videoBtn.forEach(btn =>{
    btn.addEventListener('click', ()=>{
        document.querySelector('.controls .active').classList.remove('active');
        btn.classList.add('active');
        let src = btn.getAttribute('data-src');
        document.querySelector('#video-slider').src = src;
    });
});










/*
const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('#login-btn');
const iconClose = document.querySelector('.icon-close');

registerLink.addEventListener('click', ()=> {
	wrapper.classList.add('active');
});

loginLink.addEventListener('click', ()=> {
	wrapper.classList.remove('active');
});


btnPopup.addEventListener('click', ()=> {
	wrapper.classList.add('active-popup');
});

iconClose.addEventListener('click', ()=> {
	wrapper.classList.remove('active-popup');
}); */