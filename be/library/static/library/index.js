
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Now you can safely call getCookie
const csrftoken = getCookie('csrftoken');

document.addEventListener('DOMContentLoaded', function () {
    // Show login form and hide hero section
    document.getElementById('login-button').addEventListener('click', function () {
        document.getElementById('hero-section').classList.add('hidden');
        document.getElementById('login-form').classList.remove('hidden');
    });

    // Show signup form and hide hero section
    document.getElementById('signup-button').addEventListener('click', function () {
        document.getElementById('hero-section').classList.add('hidden');
        document.getElementById('signup-form').classList.remove('hidden');
    });

    // Handle Login Form Submission
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function (event) {
            event.preventDefault(); 

            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            // Basic validation
            if (username === '' || password === '') {
                alert('Please fill in all fields.');
                return;
            }

            // AJAX request to submit the form data
            fetch('/login/', {  // Use the correct URL for login
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')  // Get CSRF token from cookie
                },
                body: JSON.stringify({
                    username: username,
                    password: password
                })
            })
            .then(response => {
                if (response.ok) {
                    window.location.href = '/'; // Redirect to home page
                } else {
                    alert('Login failed. Please check your credentials.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred. Please try again later.');
            });
        });
    }

    // Handle Registration Form Submission
    const registerForm = document.getElementById('signupForm');
    if (registerForm) {
        registerForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent the default form submission

            const username = document.getElementById('signup-username').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('signup-password').value;
            const confirmPassword = document.getElementById('confirm_password').value;

            // Basic validation
            if (username === '' || email === '' || password === '' || confirmPassword === '') {
                alert('Please fill in all fields.');
                return;
            }

            if (password !== confirmPassword) {
                alert('Passwords do not match.');
                return;
            }

            // AJAX request to submit the form data
            fetch('/register/', {  // Use the correct URL for registration
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')  // Get CSRF token from cookie
                },
                body: JSON.stringify({
                    username: username,
                    email: email,
                    password: password
                })
            })
            .then(response => {
                if (response.ok) {
                    window.location.href = '/'; // Redirect to home page
                } else {
                    alert('Registration failed. Please try again.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred. Please try again later.');
            });
        });
    }
     // Cancel buttons to go back to the hero section
    document.getElementById('cancel-login').addEventListener('click', function () {
        document.getElementById('login-form').classList.add('hidden');
        document.getElementById('hero-section').classList.remove('hidden');
    });

    document.getElementById('cancel-signup').addEventListener('click', function () {
        document.getElementById('signup-form').classList.add('hidden');
        document.getElementById('hero-section').classList.remove('hidden');
    });
});

