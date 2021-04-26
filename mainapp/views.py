from django.shortcuts import render
from django.templatetags.static import static


# Create your views here.


def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': [{'pic': static('vendor/img/products/Adidas-hoodie.png'),
                      'title': 'Худи черного цвета с монограммами adidas Originals',
                      'price': '6 090,00 руб.',
                      'text': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
                     {'pic': static('vendor/img/products/Blue-jacket-The-North-Face.png'),
                      'title': 'Синяя куртка The North Face',
                      'price': '23 725,00 руб.',
                      'text': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
                     {'pic': static('vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'),
                      'title': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                      'price': '3 390,00 руб.',
                      'text': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
                     {'pic': static('vendor/img/products/Black-Nike-Heritage-backpack.png'),
                      'title': 'Черный рюкзак Nike Heritage',
                      'price': '2 340,00 руб.',
                      'text': 'Плотная ткань. Легкий материал.'},
                     {'pic': static('vendor/img/products/Black-Dr-Martens-shoes.png'),
                      'title': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                      'price': '13 590,00 руб.',
                      'text': 'Гладкий кожаный верх. Натуральный материал.'},
                     {'pic': static('vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'),
                      'title': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                      'price': '2 890,00 руб.',
                      'text': 'Легкая эластичная ткань сирсакер Фактурная ткань.'}
                     ]
    }
    return render(request, 'mainapp/products.html', context)
