"""
URL configuration for horizweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop.views import home  # Импортируем представление для главной страницы
from django.contrib.auth import views as auth_views  # Импортируем встроенные представления для входа и выхода


urlpatterns = [
    path('', home, name='home'),  # Главная страница
    path('user/', include('user.urls')),  # Маршруты приложения user
    path('shop/', include('shop.urls')),  # Маршруты приложения shop
    path('admin/', admin.site.urls),  # Админка
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),  # Вход
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  # Выход
]

# Добавляем маршруты для медиафайлов в режиме DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)