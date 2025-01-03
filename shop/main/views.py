from django.shortcuts import redirect, render
from django.contrib import auth
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from main.models import categories, products
from main.forms import UserLoginForm, UserRegistrationForm, CustomPasswordChangeForm, UserInfoForm, PasswordResetForm
from orders.models import Order, OrderItem
from main.models import User
from django.contrib import messages
from django.db.models import Prefetch
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from shop import settings

# Create your views here.

def home(request):

    categori = categories.objects.all()
    goods = products.objects.all()
    
    data = {'title': 'MegaShop',
            'categories': categori,
            'goods': goods,
        }
    return render(request, 'main/home.html', data)

def category(request, category_slug):

    order_by = request.GET.get('order_by', None)
    
    if category_slug == 'all':
        product = products.objects.all()
        if order_by and order_by != "default":
            product = products.objects.all().order_by(order_by)
    else:
        product = products.objects.filter(category__slug=category_slug)
        if order_by and order_by != "default":
            product = products.objects.filter(category__slug=category_slug).order_by(order_by)
    
    categori = categories.objects.all()
    categoriName = categories.objects.get(slug=category_slug)
    
    data = {'title': 'Category',
            'categories': categori,
            'product': product,
            'categoriName': categoriName
        }
    return render(request, 'main/category.html', data)

def product(request, product_slug):

    categori = categories.objects.all()
    product = products.objects.get(slug=product_slug)
    
    context = {'title': 'MegaShop',
                'product': product,
                'categories': categori
        }
    return render(request, 'main/product.html', context)

def faq(request):

    categori = categories.objects.all()
    data = {'title': 'FAQ',
            'categories': categori
            }
    return render(request, 'main/faq.html', data)


def registration(request):

    categori = categories.objects.all()
    goods = products.objects.all()
    formReg = UserRegistrationForm(data=request.POST)
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        formReg = UserRegistrationForm(data=request.POST)
        if formReg.is_valid():
            formReg.save()
            user = formReg.instance
            auth.login(request, user)
            return redirect(url)
        
    data = {'title': 'MegaShop',
            'categories': categori,
            'formReg': formReg,
            'goods': goods,
            }
    return render(request, 'main/home.html', data)


def login(request):

    categori = categories.objects.all()
    goods = products.objects.all()
    form = UserLoginForm(data=request.POST)
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(url)
            
    data = {'title': 'MegaShop',
            'categories': categori,
            'form': form,
            'goods': goods,
            }
    return render(request, 'main/home.html', data)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def profile(request):

    orders = (
        Order.objects.filter(user=request.user).prefetch_related(
                Prefetch(
                    "orderitem_set",
                    queryset=OrderItem.objects.select_related("product"),
                )
            )
            .order_by("-id")
    )
    categori = categories.objects.all()
    context = {
        'orders': orders,
        'title': 'Личный кабинет',
        'categories': categori
    }
    return render(request, 'main/profile.html', context=context)


def сhangePass(request):

    orders = (
        Order.objects.filter(user=request.user).prefetch_related(
                Prefetch(
                    "orderitem_set",
                    queryset=OrderItem.objects.select_related("product"),
                )
            )
            .order_by("-id"))
    
    categori = categories.objects.all()
    form = CustomPasswordChangeForm(user=request.user, data=request.POST)
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Пароль изменен!')
            return redirect(url)
        
    data = {'title': 'Личный кабинет',
            'orders': orders,
            'categories': categori,
            'form': form,
            }
    return render(request, 'main/profile.html', data)

@login_required
def userInfo(request):

    orders = (
        Order.objects.filter(user=request.user).prefetch_related(
                Prefetch(
                    "orderitem_set",
                    queryset=OrderItem.objects.select_related("product"),
                )
            )
            .order_by("-id"))
    
    categori = categories.objects.all()
    form = UserInfoForm(request.POST, instance=request.user)
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        form = UserInfoForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные сохранены!')
            return redirect(url)
        
    data = {'title': 'Личный кабинет',
            'orders': orders,
            'categories': categori,
            'form': form,
            }
    return render(request, 'main/profile.html', data)

def passwordReset(request):

    categori = categories.objects.all()
    goods = products.objects.all()
    password_reset_form = UserLoginForm(data=request.POST)
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            mail = password_reset_form.cleaned_data['email']
            try:
                user = User.objects.get(email=mail)
            except:
                user = False
            if user:
                subject = 'Запрошен сброс пароля'
                email_template_name = 'main/password_reset_email.html'
                cont = {
                    'email': user.email,
                    'domain': '127.0.0.1:8000',
                    'site_name': 'MEGA SHOP',
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'user': user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                }
                from_email = settings.EMAIL_HOST_USER
                msg_html = render_to_string(email_template_name, cont)
                try:
                    send_mail(subject, 'ссылка', from_email, [user.email], fail_silently=False, html_message=msg_html)
                    messages.success(request, 'Письмо с инструкциями отправлено на почту!')
                except:
                    return HttpResponse('Обнаружен недопустимый заголовок!')
                return redirect('password_reset_done')
            
    data = {'title': 'MegaShop',
            'categories': categori,
            'password_reset_form': password_reset_form,
            'goods': goods,
            }
    return render(request, 'main/home.html', data)



