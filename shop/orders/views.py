from django.forms import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.db import transaction
from django.contrib import messages
from django.urls import reverse
from main.models import categories, products
from django.db.models import Prefetch

from orders.forms import CreateOrderForm
from carts.models import Cart
from orders.models import Order, OrderItem

def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        # Создать заказ
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )
                        # Создать заказанные товары
                        for cart_item in cart_items:
                            product=cart_item.product
                            name=cart_item.product.product_name
                            price=cart_item.product.sell_price()
                            quantity=cart_item.quantity


                            if product.quantity < quantity:
                                raise ValidationError(f'Недостаточное количество товара {name} на складе\
                                                       В наличии - {product.quantity}')

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity -= quantity
                            product.save()

                        # Очистить корзину пользователя после создания заказа
                        cart_items.delete()

                        messages.success(request, 'Заказ оформлен!')
                        return HttpResponseRedirect(reverse('home'))
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('orders:create_order')
    else:
        form = CreateOrderForm()

    product = products.objects.all()
    categori = categories.objects.all()
    context = {
        'title': 'Оформление заказа',
        'form': form,
        'order': True,
        'product': product,
        'categories': categori
    }
    return render(request, 'orders/create_order.html', context=context)

