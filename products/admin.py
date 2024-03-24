from django.contrib import admin

from products.models import Product, Enterprise


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'expiration_date', 'enterprise')
    list_filter = ('id', 'name', 'price', 'quantity', 'expiration_date', 'enterprise')
    search_fields = ('id', 'name', 'price', 'quantity', 'expiration_date', 'enterprise')


@admin.register(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'opening_hours', 'closing_hours', 'is_24_7')
    list_filter = ('id', 'name', 'location', 'opening_hours', 'closing_hours', 'is_24_7')
    search_fields = ('id', 'name', 'location', 'opening_hours', 'closing_hours', 'is_24_7')

