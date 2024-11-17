from django.shortcuts import redirect, render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.models import categories, products
from main.forms import UserLoginForm, UserRegistrationForm, CustomPasswordChangeForm
from orders.models import Order, OrderItem
from django.db.models import Prefetch
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def home(request):

    back_url = request.path

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(back_url)
    else:
        form = UserLoginForm()

    categori = categories.objects.all()
    goods = products.objects.all()
    
    data = {'title': 'MegaShop',
            'form': form,
            'categories': categori,
            'goods': goods,
        }
    return render(request, 'main/home.html', data)

def category(request, category_slug):

    order_by = request.GET.get('order_by', None)
    back_url = request.path
    
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(back_url)
    else:
        form = UserLoginForm()
    
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
            'form': form,
            'categories': categori,
            'product': product,
            'categoriName': categoriName
        }
    return render(request, 'main/category.html', data)



def product(request, product_slug):

    back_url = request.path

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(back_url)
    else:
        form = UserLoginForm()

    categori = categories.objects.all()
    product = products.objects.get(slug=product_slug)
    
    context = {'title': 'MegaShop',
               'form': form,
            'product': product,
            'categories': categori
        }
    return render(request, 'main/product.html', context)


def faq(request):

    back_url = request.path

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(back_url)
    else:
        form = UserLoginForm()

    categori = categories.objects.all()
    data = {'title': 'FAQ',
            'form': form,
            'categories': categori
            }
    return render(request, 'main/faq.html', data)

def registration(request):
    
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = UserRegistrationForm()

    categori = categories.objects.all()
    data = {'title': 'Registration',
            'form': form,
            'categories': categori
            }
    return render(request, 'main/registration.html', data)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def profile(request):

    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = CustomPasswordChangeForm(user=request.user)

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
        'form': form,
        'title': 'Личный кабинет',
        'categories': categori
    }
    return render(request, 'main/profile.html', context=context)
