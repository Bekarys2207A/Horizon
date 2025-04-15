from django.contrib import admin
from .models import Category, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)                      # отображать имя
    search_fields = ('name',)                     # поиск по имени

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_at')  # отображаемые поля
    search_fields = ('name',)                                  # поле поиска
    list_filter = ('category', 'created_at')                   # фильтры справа
