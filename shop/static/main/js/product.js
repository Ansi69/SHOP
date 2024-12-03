window.onload = function() {

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
    
    // Отображение выбранного размера
    
    let sizes = document.querySelectorAll('.size');
    
    sizes.forEach(size => {  
        size.addEventListener('click', function() {
        document.querySelector(".size.activeSize").classList.remove('activeSize');
        this.classList.add('activeSize');
        })
    })
}