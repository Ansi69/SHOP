let modal = document.getElementById('loginModal');

function showLogin() {
    modal.style.display = 'block';
}

function closeLogin() {
    modal.style.display = 'none';
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
