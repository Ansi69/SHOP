function showCart() {
    document.getElementById('cart_items_container').style.display = 'block';
}

function closeCart() {
    document.getElementById('cart_items_container').style.display = 'none';
}

function showLogin() {
    document.getElementById('loginModal').style.display = 'block';
}

function closeLogin() {
    document.getElementById('loginModal').style.display = 'none';
}

window.onclick = function(event) {
    if (event.target == loginModal) {
        loginModal.style.display = "none";
    }
    if (event.target == cart_items_container) {
        cart_items_container.style.display = "none";
    }
}


// При загрузке страницы
window.onload = function() {
        document.getElementById('loginModal').style.display = 'none';
    }
;


// При загрузке страницы
window.onload = function() {
    if (document.getElementById('ErrorForm').style.display === 'none') {
        closeLogin()
    }
    else{
        showLogin();
    }
};