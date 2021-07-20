from django.shortcuts import render
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView

from mainapp.models import Product, ProductCategory
from django.conf import settings
from django.core.cache import cache


def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'mainapp/base.html', context)


# def products(request, category_id=None, page=1):
#     context = {
#         'title': 'GeekShop - Каталог',
#         'categories': ProductCategory.objects.all()
#     }
#     products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
#     paginator = Paginator(products, per_page=3)
#     try:
#         products_paginator = paginator.page(page)
#     except PageNotAnInteger:
#         products_paginator = paginator.page(1)
#     except EmptyPage:
#         products_paginator = paginator.page(paginator.num_pages)
#     context.update({'products': products_paginator})
#     return render(request, 'mainapp/products.html', context)

def get_links_menu():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.all()
            cache.set(key, links_menu)
        return links_menu
    else:
        return ProductCategory.objects.all()


class ProductsList(ListView):
    model = Product
    template_name = 'mainapp/products.html'
    paginate_by = 3

    def get_queryset(self):
        if self.kwargs.get('pk'):
            return super(ProductsList, self).get_queryset().filter(category_id=self.kwargs.get('pk')).order_by('name')
        else:
            return super(ProductsList, self).get_queryset()

    def get_context_data(self, **kwargs):
        context = super(ProductsList, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Каталог'
        context['categories'] = get_links_menu()  # ProductCategory.objects.all()

        return context
