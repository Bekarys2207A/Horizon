from django.contrib import admin
from .models import User, SellerApplication

# Регистрация модели User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_seller', 'is_staff', 'is_active')  # Поля для отображения
    search_fields = ('email', 'username')  # Поля для поиска
    list_filter = ('is_seller', 'is_staff', 'is_active')  # Фильтры

# Регистрация модели SellerApplication
@admin.register(SellerApplication)
class SellerApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'status')  # Поля для отображения
    search_fields = ('user__email',)  # Поля для поиска
    list_filter = ('status',)  # Фильтры