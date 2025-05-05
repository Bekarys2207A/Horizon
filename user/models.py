from django.contrib.auth.models import AbstractUser
from django.db import models
import random

class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Почта")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Номер телефона")
    is_seller = models.BooleanField(default=False, verbose_name="Продавец")
    activation_code = models.CharField(max_length=6, blank=True, null=True, verbose_name="Код активации")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def generate_activation_code(self):
        """Генерация 6-значного кода активации"""
        self.activation_code = str(random.randint(100000, 999999))
        self.save()


class SellerApplication(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')],
        default='pending',
        verbose_name="Статус"
    )

    def __str__(self):
        return f"{self.user.email} - {self.status}"