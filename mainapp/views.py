from django.shortcuts import render
from django.templatetags.static import static
from mainapp.models import Product, ProductCategory
import json

# Create your views here.


def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    with open("mainapp/fixtures/products.json", "r", encoding='UTF-8') as products_json:
        products_context = json.load(products_json)

    for product in products_context:
        product['image'] = static(product['image'])

    context = {
        'title': 'GeekShop - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'mainapp/products.html', context)
