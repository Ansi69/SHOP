// Смена при загрузке страницы валют
document.addEventListener('DOMContentLoaded', () => {

    const rubButton = document.getElementById('rubButton');
    const usdButton = document.getElementById('usdButton');
    
    function setCurrency(currency) {
        localStorage.setItem('currency', currency);
    }
    
    const savedCurrency = localStorage.getItem('currency');

    switch (savedCurrency) {
        case 'rub':
            setCurrency('rub');
        break;
        case 'usd':
            setCurrency('usd');
        break;
    }


    const currencyElements = document.querySelectorAll(`[data-currency-${savedCurrency}]`);
    currencyElements.forEach(function (item) {
        const currenValue =  item.getAttribute(`data-currency-${savedCurrency}`)

        item.innerHTML = currenValue
    })


    
    rubButton.addEventListener('click', () => {
        setCurrency('rub');
    });
        
    usdButton.addEventListener('click', () => {
        setCurrency('usd');
    });
});
