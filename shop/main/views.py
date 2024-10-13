from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.models import categories, products
from main.forms import UserLoginForm, UserRegistrationForm
from orders.models import Order, OrderItem

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
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

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
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
    
    data = {'title': 'Category',
            'form': form,
            'categories': categori,
            'product': product,
        }
    return render(request, 'main/category.html', data)



def product(request, product_slug):

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
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

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
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
