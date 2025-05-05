from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserRegistrationForm
from .models import User, SellerApplication
from django.contrib.auth.decorators import login_required
import random

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  # Устанавливаем пароль
            user.is_active = False  # Делаем пользователя неактивным до активации
            user.save()

            # Генерация и отправка кода активации
            user.activation_code = str(random.randint(100000, 999999))
            user.save()
            send_mail(
                'Код активации',
                f'Ваш код активации: {user.activation_code}',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )

            return redirect('activate-account')  # Перенаправляем на страницу активации
    else:
        form = UserRegistrationForm()
    return render(request, 'auth/register.html', {'form': form})


def activate_account(request):
    if request.method == 'POST':
        code = request.POST.get('activation_code')
        try:
            user = User.objects.get(activation_code=code)
            user.is_active = True
            user.activation_code = None  # Удаляем код активации после успешной активации
            user.save()
            return redirect('login')  # Перенаправляем на страницу входа
        except User.DoesNotExist:
            return render(request, 'auth/activate_account.html', {'error': 'Неверный код активации'})
    return render(request, 'auth/activate_account.html')


@login_required
def apply_seller(request):
    if request.method == 'POST':
        # Создаем заявку на статус продавца
        SellerApplication.objects.create(user=request.user)
        return redirect('home')  # Перенаправляем на главную страницу после отправки заявки
    return render(request, 'auth/apply_seller.html')