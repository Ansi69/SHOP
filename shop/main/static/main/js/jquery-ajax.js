$(document).ready(function () {
    var successMessage = $("#jq-notification");

    $(document).on("click", ".add-to-cart", function (e) {
        e.preventDefault();

        var goodsInCartCount = $("#goods-in-cart-count");
        var cartCount = parseInt(goodsInCartCount.text() || 0);
        var product_id = $(this).data("product-id");
        var add_to_cart_url = $(this).attr("href");

        // делаем post запрос через ajax не перезагружая страницу
        $.ajax({
            type: "POST",
            url: add_to_cart_url,
            data: {
                product_id: product_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 3000);

                cartCount++;
                goodsInCartCount.text(cartCount);
                var cartItemsContainer = $("#cart_items");
                cartItemsContainer.html(data.cart_items_html);

            },
            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });
    });

    // Ловим событие клика по кнопке удалить товар из корзины
    $(document).on("click", ".remove-from-cart", function (e) {
        e.preventDefault();

        var goodsInCartCount = $("#goods-in-cart-count");
        var cartCount = parseInt(goodsInCartCount.text() || 0);
        var cart_id = $(this).data("cart-id");
        var remove_from_cart = $(this).attr("href");

        $.ajax({

            type: "POST",
            url: remove_from_cart,
            data: {
                cart_id: cart_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 3000);

                cartCount -= data.quantity_deleted;
                goodsInCartCount.text(cartCount);
                var cartItemsContainer = $("#cart_items");
                cartItemsContainer.html(data.cart_items_html);
            },

            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });
    });
    
    // Обработчик события для уменьшения значения
    $(document).on("click", ".decrement", function () {
        var url = $(this).data("cart-change-url");
        var cartID = $(this).data("cart-id");
        var $input = $(this).closest('.productCountAndPriceCart').find('.numberProductsCart');
        var currentValue = parseInt($input.val());
        if (currentValue > 1) {
            $input.val(currentValue - 1);
            updateCart(cartID, currentValue - 1, -1, url, 0);
        }
    });


    // Обработчик события для увеличения значения
    $(document).on("click", ".increment", function () {
        var url = $(this).data("cart-change-url");
        var cartID = $(this).data("cart-id");
        var $input = $(this).closest('.productCountAndPriceCart').find('.numberProductsCart');
        var currentValue = parseInt($input.val());

        $input.val(currentValue + 1);
        updateCart(cartID, currentValue + 1, 1, url, 0);
    });


    // Обработчик события для удаления
    $(document).on("click", ".delete", function () {
        var url = $(this).data("cart-change-url");
        var cartID = $(this).data("cart-id");
        var $input = $(this).closest('.productCountAndPriceCart').find('.numberProductsCart');
        var currentValue = parseInt($input.val());

        $input.val(currentValue - 1);
        updateCart(cartID, currentValue - 1, 1, url, 1);
    });


    function updateCart(cartID, quantity, change, url, penis) {
        $.ajax({
            type: "POST",
            url: url,
            data: {
                cart_id: cartID,
                quantity: quantity,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },

            success: function (data) {
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 3000);

                var goodsInCartCount = $("#goods-in-cart-count");
                var cartCount = parseInt(goodsInCartCount.text() || 0);
                if (penis == 0) {
                    cartCount += change;
                }
                else {
                    cartCount -= change;
                }
                goodsInCartCount.text(cartCount);
                var cartItemsContainer = $("#cart_items");
                cartItemsContainer.html(data.cart_items_html);

            },
            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });
    }


// Обработчик события радиокнопки выбора способа доставки
$("input[name='requires_delivery']").change(function () {
    var selectedValue = $(this).val();
    // Скрываем или отображаем input ввода адреса доставки
    if (selectedValue === "1") {
        $("#deliveryAddressField").show();
    } else {
        $("#deliveryAddressField").hide();
    }
});

    // Форматирования ввода номера телефона в форме (xxx) xxx-хххx
    document.getElementById('id_phone_number').addEventListener('input', function (e) {
        var x = e.target.value.replace(/\D/g, '').match(/(\d{0,3})(\d{0,3})(\d{0,4})/);
        e.target.value = !x[2] ? x[1] : '(' + x[1] + ') ' + x[2] + (x[3] ? '-' + x[3] : '');
    });

    // Проверяем на стороне клинта коррекность номера телефона в форме xxx-xxx-хх-хx
    $('#create_order_form').on('submit', function (event) {
        var phoneNumber = $('#id_phone_number').val();
        var regex = /^\(\d{3}\) \d{3}-\d{4}$/;

        if (!regex.test(phoneNumber)) {
            $('#phone_number_error').show();
            event.preventDefault();
        } else {
            $('#phone_number_error').hide();

            // Очистка номера телефона от скобок и тире перед отправкой формы
            var cleanedPhoneNumber = phoneNumber.replace(/[()\-\s]/g, '');
            $('#id_phone_number').val(cleanedPhoneNumber);
        }
    });
});