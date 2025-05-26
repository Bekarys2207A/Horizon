from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.shortcuts import redirect
from django.contrib import messages

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ProductForm


from django.views.generic.detail import DetailView

def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})

def about(request):
    return render(request, 'shop/about.html')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('cart')

def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'shop/category_products.html', {
        'category': category,
        'products': products
    })

def cart_view(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = []
    for product in products:
        cart_items.append({
            'product': product,
            'quantity': cart[str(product.id)],
        })
    return render(request, 'shop/cart.html', {'cart_items': cart_items})



def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('product-detail', pk=product_id)

def home(request):
    query = request.GET.get('q')
    products = Product.objects.all()
    if query:
        products = products.filter(name__icontains=query)
    return render(request, 'shop/home.html', {'products': products})

def make_order(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')
        # Здесь можно сохранить заказ в базу или отправить уведомление
        messages.success(request, 'Ваш заказ успешно оформлен!')
        # Очистить корзину
        request.session['cart'] = {}
        return redirect('cart')
    return redirect('cart')

class ProductListView(ListView):
    model = Product
    template_name = 'shop/product_list.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'shop/product_form.html'
    success_url = reverse_lazy('product-list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'shop/product_form.html'
    success_url = reverse_lazy('product-list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'shop/product_confirm_delete.html'
    success_url = reverse_lazy('product-list')
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'