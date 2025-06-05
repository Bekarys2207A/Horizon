from modeltranslation.translator import register, TranslationOptions
from .models import Category, Product

@register(Category)
class CategoryTranslation(TranslationOptions):
    fields = ('name',)

@register(Product)
class ProductTranslation(TranslationOptions):
    fields = ('name', 'description',)
