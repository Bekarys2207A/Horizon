from django.urls import path
from .views import (
    home,
    about,
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

urlpatterns = [
    path('', home, name='home'),  # Главная страница магазина
    path('about/', about, name='about'),  # Страница "О нас"
    path('products/', ProductListView.as_view(), name='product-list'),  # Список продуктов
    path('products/create/', ProductCreateView.as_view(), name='product-create'),  # Создание продукта
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),  # Обновление продукта
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),  # Удаление продукта
]