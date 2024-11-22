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
    document.getElementById('registerModal').style.display = 'none';
    hideScroll()
}

function showReg() {
    document.getElementById('loginModal').style.display = 'none';
    document.getElementById('registerModal').style.display = 'block';
    hideScroll()
}

function closeReg() {
    document.getElementById('registerModal').style.display = 'none';
    showScroll()
}

function closeLogin() {
    document.getElementById('loginModal').style.display = 'none';
    showScroll()
}

window.onclick = function(event) {
    if (event.target == loginModal) {
        closeLogin()
    }
    if (event.target == registerModal) {
        closeReg()
    }
    if (event.target == cart_items_container) {
        closeCart()
    }
}


// Отображение форм, при наличии в них ошибок

window.onload = function() { 

    // Поиск элемента с ошибкой
    const logError = document.getElementById('ErrorForm'); 
    const regError = document.getElementById('ErrorForm2'); 

    // Проверяем, нужно ли закрыть эти ебанные формы
    const loginClosed = sessionStorage.getItem('loginClosed') === 'true';
    const regClosed = sessionStorage.getItem('regClosed') === 'true';

    // Форма с Входом
    if (logError === null || loginClosed) { 
        closeLogin(); 
    } else { 
        showLogin(); 
        sessionStorage.setItem('loginClosed', 'true');
    } 

    // Форма с Регистрацией
    if (regError === null || regClosed) { 
        closeReg(); 
    } else { 
        showReg();
        sessionStorage.setItem('regClosed', 'true'); 
    } 

    // Отслеживание события отправки формы
    document.getElementById('loginModal').addEventListener('submit', function() {
        sessionStorage.setItem('loginClosed', 'false');
    });

    document.getElementById('registerModal').addEventListener('submit', function() {
        sessionStorage.setItem('regClosed', 'false');
    });



};

