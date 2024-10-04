function showCart() {
    document.getElementById('cart_items_container').style.display = 'block';
}

function closeCart() {
    document.getElementById('cart_items_container').style.display = 'none';
}

window.onclick = function(event) {
    if (event.target == cart_items_container) {
        cart_items_container.style.display = "none";
    }
}