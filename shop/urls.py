from django.urls import path
from .views import make_order
from .views import (

    home,
    about,
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    category_products,
    ProductDetailView,  
    cart_view,       
    add_to_cart, 
    remove_from_cart,
)

urlpatterns = [
    path('', home, name='home'),  
    path('about/', about, name='about'),  
    path('products/', ProductListView.as_view(), name='product-list'), 
    path('products/create/', ProductCreateView.as_view(), name='product-create'),  
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),  
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'), 
    path('category/<slug:slug>/', category_products, name='category_products'), 
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),  
    path('cart/', cart_view, name='cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add-to-cart'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove-from-cart'),
    path('make-order/', make_order, name='make-order'),
]