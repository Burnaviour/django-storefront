from django.contrib import admin
# Register your models here.
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory', 'last_update']
    list_editable = ['unit_price', 'inventory']
    list_per_page = 10
    # list_filter = ['last_update']
    # search_fields = ['title']


admin.site.register(models.Collection)
