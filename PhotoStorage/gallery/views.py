from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

def product_list(request):

    products = Product.objects.all()
    context = {
        'products' : products
    }

    return render(request , 'gallery/index.html' , context)


def home(request):
    
    return HttpResponse('this is home')

