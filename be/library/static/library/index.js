document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('login-button').addEventListener('click', function () {
        document.getElementById('hero-section').classList.add('hidden');
        document.getElementById('login-form').classList.remove('hidden');
    });

    document.getElementById('signup-button').addEventListener('click', function () {
        document.getElementById('hero-section').classList.add('hidden');
        document.getElementById('signup-form').classList.remove('hidden');
    });

    document.getElementById('cancel-login').addEventListener('click', function () {
        document.getElementById('login-form').classList.add('hidden');
        document.getElementById('hero-section').classList.remove('hidden');
    });

    document.getElementById('cancel-signup').addEventListener('click', function () {
        document.getElementById('signup-form').classList.add('hidden');
        document.getElementById('hero-section').classList.remove('hidden');
    });
});

