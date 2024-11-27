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
            case this.className.includes("navPasswrd"):
                document.querySelector(".tab.activeTab").classList.remove('activeTab');
                document.querySelector(".profilePasswrd").classList.add('activeTab');
            break;
            case this.className.includes("navAdditSett"):
                document.querySelector(".tab.activeTab").classList.remove('activeTab');
                document.querySelector(".profileAdditSett").classList.add('activeTab');
            break;
        }
      })
    });




    // Отображение выбранной темы

    let themes = document.querySelectorAll('.theme');

    // Если тема у пользователя была выбрана светлая
    if(localStorage.getItem('theme') == 'light') {
        document.querySelector(".theme.activeTheme").classList.remove('activeTheme');
        document.querySelector(".theme.lightTheme").classList.add('activeTheme');
        }
    
    themes.forEach(theme => {
        theme.addEventListener('click', function () {
            document.querySelector(".theme.activeTheme").classList.remove('activeTheme');
            this.classList.add('activeTheme');
        })
    });




        // Отображение выбранной валюты

        let currencys = document.querySelectorAll('.currency');

        // Если тема у пользователя была выбрана светлая
        if(localStorage.getItem('currency') == 'usd') {
            document.querySelector(".currency.activeCurrency").classList.remove('activeCurrency');
            document.querySelector(".currency.usdCurrency").classList.add('activeCurrency');
            }
        
        currencys.forEach(currency => {
            currency.addEventListener('click', function () {
                document.querySelector(".currency.activeCurrency").classList.remove('activeCurrency');
                this.classList.add('activeCurrency');
            })
        });



    //Отображение вкладки со сменой пароля, при наличии в ней ошибки

    // Поиск элемента с ошибкой
    const passChangeError = document.getElementById('ErrorForm5');

    // Проверяем, нужно ли закрыть эти ебанную вкладку
    const passChangeClosed = sessionStorage.getItem('passChangeClosed') === 'true';


    // Вкладка со сменой пароля
    if (passChangeError === null || passChangeClosed) { 

    } else {
        document.querySelector(".nav.activeNav").classList.remove('activeNav');
        document.querySelector(".nav.navPasswrd").classList.add('activeNav');

        document.querySelector(".tab.activeTab").classList.remove('activeTab');
        document.querySelector(".profilePasswrd").classList.add('activeTab');
        
        sessionStorage.setItem('passChangeClosed', 'true');
    }

    // Отслеживание события отправки формы
    document.getElementById('passChangeModal').addEventListener('submit', function() {
        sessionStorage.setItem('passChangeClosed', 'false');
    });



    // Убрать внизу ошибку с - Обязательными полями
    const firstLi = document.querySelector('#ErrorForm5 li')
    if(firstLi.innerHTML == 'Обязательное поле.') {
        passChangeError.style.display = "none";
    }






};   







