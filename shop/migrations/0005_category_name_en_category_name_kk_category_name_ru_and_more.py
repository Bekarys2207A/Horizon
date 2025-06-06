# Generated by Django 5.2 on 2025-06-04 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Название категории'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_kk',
            field=models.CharField(max_length=100, null=True, verbose_name='Название категории'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Название категории'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_kk',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Название товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_kk',
            field=models.CharField(max_length=255, null=True, verbose_name='Название товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название товара'),
        ),
    ]
