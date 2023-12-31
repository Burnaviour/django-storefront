from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.urls import reverse
from django.db.models import Count
from django.utils.html import format_html, urlencode
# Register your models here.
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price',
                    'inventory_status', 'collection__title']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']
    # list_filter = ['last_update']
    # search_fields = ['title']

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        return 'Low' if product.inventory < 10 else 'Ok'

    def collection__title(self, product):
        return product.collection.title


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
    # list_filter = ['last_update']
    # search_fields = ['title']

    def orders(self, customer):
        url = (reverse('admin:store_order_changelist')
               + '?'
               + urlencode({
                   'customer__id': str(customer.id)
               })

               )
        return format_html('<a href="{}">{} Orders</a>', url,
                           customer.orders_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(

            orders_count=Count('order')
        )


@admin.register(models.Order)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']
    list_per_page = 10
    list_select_related = ['customer']
    # list_filter = ['last_update']
    # search_fields = ['title']


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    # list_filter = ['last_update']
    # search_fields = ['title']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (reverse('admin:store_product_changelist')
               + '?'
               + urlencode({
                   'collection__id': str(collection.id)
               })

               )
        return format_html('<a href="{}">{}</a>', url,
                           collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(products_count=Count('product'))
