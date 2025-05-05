from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('activate/', views.activate_account, name='activate-account'),
    path('apply-seller/', views.apply_seller, name='apply-seller'),
]