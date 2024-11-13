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
        closeLogin()
    }
    if (event.target == cart_items_container) {
        closeCart()
    }
}

// При загрузке страницы
window.onload = function() {
    if (document.getElementById('ErrorForm').style.display === 'none') {
        closeLogin()
    }
    else{
        showLogin();
    }
};




window.onload = function() {

// Покраска статуса заказа

let statusOrder = document.querySelectorAll('.orderStatus');
for(let element of statusOrder)  
{
    switch (element.innerHTML) {
    case "В обработке":
        element.style.color = "#00C30D";
    break;
    case "Отменен":
        element.style.color = "#FF4848";
    break;}
}


// Отображение выбранной вкладки в профиле

let btns = document.querySelectorAll('.nav');

btns.forEach(btn => {  
    btn.addEventListener('click', function() {
    document.querySelector(".nav.activeNav").classList.remove('activeNav');
    this.classList.add('activeNav');

    // Проверка на то, на какую вкладку нажали
    switch (true) {
        case this.className.includes("navPersnInf"):
            document.querySelector(".tab.activeTab").classList.remove('activeTab');
            document.querySelector(".profileInf").classList.add('activeTab');
        break;
        case this.className.includes("navMyOrders"):
            document.querySelector(".tab.activeTab").classList.remove('activeTab');
            document.querySelector(".profileMyOrders").classList.add('activeTab');
        break;
        case this.className.includes("navAdditSett"):
            document.querySelector(".tab.activeTab").classList.remove('activeTab');
            document.querySelector(".profileAdditSett").classList.add('activeTab');
        break;
    }
  })
});




// Отображение выбранного размера

let sizes = document.querySelectorAll('.size');

sizes.forEach(size => {  
    size.addEventListener('click', function() {
    document.querySelector(".size.activeSize").classList.remove('activeSize');
    this.classList.add('activeSize');
    })
})





// Переключение темы


 let themes = document.querySelectorAll('.theme');

 // Если тема у пользователя была выбрана светлая
 if(localStorage.getItem('theme') == 'false') {
    themeLink.setAttribute('href', "/static/main/css/lightTheme.css")
    document.querySelector(".theme.activeTheme").classList.remove('activeTheme');
    document.querySelector(".theme.lightTheme").classList.add('activeTheme');
  }

 themes.forEach(theme => {
    theme.addEventListener('click', function () {
        document.querySelector(".theme.activeTheme").classList.remove('activeTheme');
        this.classList.add('activeTheme');
        if(theme.classList.contains('lightTheme')) {
            themeLink.setAttribute('href', '/static/main/css/lightTheme.css')
            localStorage.setItem('theme',false)
        }
        else{
            themeLink.setAttribute('href', '/static/main/css/home.css')
            localStorage.setItem('theme',true)
        }
     })
 });





// ЕСЛИ ЧТО ВДРУГ НЕ ПИШИ КОД НИЖЕ СЛАЙДЕРА А ТО ПИЗДЕЦ ВСЕМУ!!!!!!



// Слайдер



function nodesToArray (nodes, skip = 0) {
    return Array.prototype.slice.call(nodes,skip)
}


// Добавление точек под картинкой в зависимости от количества картинокв
const newSlides = document.querySelectorAll('.slide');

let newDots = nodesToArray(newSlides, 1);
let index = 1;

for (dot of newDots) {
    let newDot = document.createElement("div"); 
    newDot.className = "dot";
    newDot.setAttribute("data-index",index)
    document.querySelector(".dots").append(newDot);
    index++;
}


// Выбор необходимых элементов
const slides = document.querySelector('.slides');
const dots = document.querySelectorAll('.dot');
const arrowLeft = document.querySelector('.arrowLeft');
const arrowRight = document.querySelector('.arrowRight');
let currentIndex = 0;



// Процесс обновления слайдера (листание картинок) 
function updateSlider(index) {
    slides.style.transform = `translateX(${-index * 100}%)`;
    dots.forEach(dot => dot.classList.remove('activeDot'));
    dots[index].classList.add('activeDot');
}

// Взамодействие с левой стрелкой
arrowLeft.addEventListener('click', () => { 
    currentIndex = (currentIndex === 0) ? dots.length - 1 : currentIndex - 1; 
    updateSlider(currentIndex); 
}); 

// Взамодействие с правой стрелкой
arrowRight.addEventListener('click', () => {
    currentIndex = (currentIndex === dots.length - 1) ? 0 : currentIndex + 1;
    updateSlider(currentIndex);
});

// Взамодействие с точками
dots.forEach(dot => {
    dot.addEventListener('click', () => {
        currentIndex = Number(dot.dataset.index);
        updateSlider(currentIndex);
    });
});



// ЕСЛИ ЧТО ВДРУГ НЕ ПИШИ КОД НИЖЕ СЛАЙДЕРА А ТО ПИЗДЕЦ ВСЕМУ!!!!!!






}


