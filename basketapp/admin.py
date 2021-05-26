from django.contrib import admin
from basketapp.models import Basket


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('created_timestamp', 'user', 'product', 'quantity')
    fields = ('user', 'product', 'quantity')
