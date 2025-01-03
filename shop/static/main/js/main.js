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

function showReset() {
    document.getElementById('loginModal').style.display = 'none';
    document.getElementById('resetModal').style.display = 'block';
    hideScroll()
}

function closeReset() {
    document.getElementById('resetModal').style.display = 'none';
    showScroll()
}

function backReset() {
    document.getElementById('resetModal').style.display = 'none';
    document.getElementById('loginModal').style.display = 'block';
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
    if (event.target == resetModal) {
        closeReset()
    }
}


// Отображение форм, при наличии в них ошибок

window.onload = function() { 

    // Поиск элемента с ошибкой
    const logError = document.getElementById('ErrorForm'); 
    const regError = document.getElementById('ErrorForm2');
    const resetError = document.getElementById('ErrorForm3');

    // Проверяем, нужно ли закрыть эти ебанные формы
    const loginClosed = sessionStorage.getItem('loginClosed') === 'true';
    const regClosed = sessionStorage.getItem('regClosed') === 'true';
    const resetClosed = sessionStorage.getItem('resetClosed') === 'true';

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

    // Форма со сбросом пароля
    if (resetError === null || resetClosed) { 
        closeReset(); 
    } else { 
        showReset();
        sessionStorage.setItem('resetClosed', 'true'); 
    } 

    // Отслеживание события отправки формы
    document.getElementById('loginModal').addEventListener('submit', function() {
        sessionStorage.setItem('loginClosed', 'false');
    });

    document.getElementById('registerModal').addEventListener('submit', function() {
        sessionStorage.setItem('regClosed', 'false');
    });

    document.getElementById('resetModal').addEventListener('submit', function() {
        sessionStorage.setItem('resetClosed', 'false');
    });





};




function togglePaymentFields() {
    const paymentMethod = document.querySelector('input[name="payment_method"]:checked').value;
    const cardFields = document.getElementById('card-fields');

    if (paymentMethod === 'card') {
        cardFields.style.display = 'block'; // Показываем поля для ввода данных карты
    } else {
        cardFields.style.display = 'none'; // Скрываем поля для ввода данных карты
    }
}