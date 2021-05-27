from django.urls import path
# from mainapp.views import products
from mainapp.views import ProductsList

app_name = 'mainapp'

urlpatterns = [
    # path('', products, name='index'),
    # path('<int:category_id>/', products, name='product'),
    # path('page/<int:page>/', products, name='page'),
    path('', ProductsList.as_view(), name='index'),
    path('<int:pk>/', ProductsList.as_view(), name='product'),
    path('page/<int:page>/', ProductsList.as_view(), name='page'),
]
