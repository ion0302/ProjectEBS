from django.contrib import admin

from .models import Product, Image


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'date', 'photo')
    search_fields = ('id', 'name', 'description', 'price')
    list_editable = ('price', 'description')


admin.site.register(Product)
admin.site.register(Image)
