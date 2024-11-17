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
};   