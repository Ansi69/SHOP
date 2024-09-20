from django.shortcuts import render

# Create your views here.

def home(request):
    data = {'title': 'MEGA|SHOP'
            ''}
    return render(request, 'main/home.html', data)

def faq(request):
    data = {'title': 'FAQ'
            ''}
    return render(request, 'main/faq.html', data)