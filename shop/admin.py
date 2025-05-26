from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}  # Добавьте эту строку

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_at')
    search_fields = ('name',)
    list_filter = ('category', 'created_at')
    fields = ('name', 'category', 'price', 'description', 'image')