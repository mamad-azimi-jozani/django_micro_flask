from django.contrib import admin

from .models import Product, User

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    pass
