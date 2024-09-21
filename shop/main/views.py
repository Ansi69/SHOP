from django.shortcuts import render
from main.models import categories, products

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
    
    if category_slug == 'all':
        product = products.objects.all()
    else:
        product = products.objects.filter(category__slug=category_slug)

    categori = categories.objects.all()
    
    data = {'title': 'MegaShop',
            'categories': categori,
            'product': product,
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