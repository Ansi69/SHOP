document.addEventListener('DOMContentLoaded', () => {

    const lightButton = document.getElementById('lightButton');
    const darkButton = document.getElementById('darkButton');
    const body = document.body;

    function setTheme(theme) {
        body.className = theme;
        localStorage.setItem('theme', theme);
    }

    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        setTheme(savedTheme);
    } else {
        setTheme('light');
    }

    lightButton.addEventListener('click', () => {
        setTheme('light');
    });

    darkButton.addEventListener('click', () => {
        setTheme('dark');
    });
});