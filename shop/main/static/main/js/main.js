// отключение прокрутки страницы
function hideScroll(){
    document.body.style.overflow = "hidden";
}

// включение прокрутки 
function showScroll(){
    document.body.style.overflow = "auto";
}


function showCart() {
    document.getElementById('cart_items_container').style.display = 'block';
    hideScroll()
}

function closeCart() {
    document.getElementById('cart_items_container').style.display = 'none';
    showScroll()
}

function showLogin() {
    document.getElementById('loginModal').style.display = 'block';
    hideScroll()
}

function closeLogin() {
    document.getElementById('loginModal').style.display = 'none';
    showScroll()
}

window.onclick = function(event) {
    if (event.target == loginModal) {
        loginModal.style.display = "none";
        showScroll()
    }
    if (event.target == cart_items_container) {
        cart_items_container.style.display = "none";
        showScroll()
    }
}


// При загрузке страницы
window.onload = function() {
        document.getElementById('loginModal').style.display = 'none';
        showScroll()
    }
;


// При загрузке страницы
window.onload = function() {
    if (document.getElementById('ErrorForm').style.display === 'none') {
        closeLogin()
        showScroll()
    }
    else{
        showLogin();
    }
};