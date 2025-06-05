from django.contrib import admin
from .models import Category, Product
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        (_('Основная информация'), {
            "fields": ('slug',)
        }),
        (_('Информация о категории (Русский)'), {
            "fields": ('name_ru',)
        }),
        (_('Информация о категории (Английский)'), {
            "fields": ('name_en',)
        }),
        (_('Информация о категории (Казахский)'), {
            "fields": ('name_kk',)
        }),
    )

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('name', 'category', 'price', 'created_at')
    search_fields = ('name',)
    list_filter = ('category', 'created_at')
    fieldsets = (
        (_('Основная информация'), {
            "fields": ('category', 'price', 'image')
        }),
        (_('Информация о товаре (Русский)'), {
            "fields": ('name_ru', 'description_ru')
        }),
        (_('Информация о товаре (Английский)'), {
            "fields": ('name_en', 'description_en')
        }),
        (_('Информация о товаре (Казахский)'), {
            "fields": ('name_kk', 'description_kk')
        }),
    )
