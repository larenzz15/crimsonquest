const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnB');
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
});


document.addEventListener("DOMContentLoaded", function () {
	// Kunin ang button na may class "btn" (Log in button)
	var loginButton = document.querySelector(".btn");

	// I-attach ang event listener para sa click event sa button
	loginButton.addEventListener("click", function (event) {
		// Kunin ang email at password na inilagay ng user
		var emailInput = document.querySelector('input[type="email"]');
		var passwordInput = document.querySelector('input[type="password"]');

		// Gawing redirect ang user sa panibagong HTML page
		if (emailInput.value.includes("@gmail.com") && emailInput.value.trim() !== "" && passwordInput.value.trim() !== "") {
            window.location.href = "map.html";
        } else {
            if (!emailInput.value.trim() || !passwordInput.value.trim()) {
                alert("Please enter both email and password.");
            } else {
                alert("Kindly input your email address.");
            }
        }

		// Ito ay upang pigilin ang default behavior ng form submission
		event.preventDefault();
	});
});
