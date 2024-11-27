from django.forms import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.db import transaction
from django.contrib import messages
from django.urls import reverse
from main.models import categories, products
from django.db.models import Prefetch
from orders.email import send_html_email

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
                            region=form.cleaned_data['region'],
                            city=form.cleaned_data['city'],
                            street=form.cleaned_data['street'],
                            postcode=form.cleaned_data['postcode'],
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
                        subject = form.cleaned_data['first_name']
                        to_email = form.cleaned_data['email']
                        num = order.id
                        region=form.cleaned_data['region']
                        city=form.cleaned_data['city']
                        street=form.cleaned_data['street']
                        return HttpResponseRedirect(reverse('home'),send_html_email(subject, to_email, num, region, city, street))
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

