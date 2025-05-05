import uuid
from django.db import migrations, models


def set_default_activation_code(apps, schema_editor):
    User = apps.get_model('user', 'User')
    for user in User.objects.all():
        try:
            # Проверяем, если значение некорректное, устанавливаем новый UUID
            uuid.UUID(str(user.activation_code))
        except (ValueError, TypeError):
            user.activation_code = uuid.uuid4()
            user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_activation_code'),
    ]

    operations = [
        migrations.RunPython(set_default_activation_code),  # Устанавливаем значения для существующих записей
        migrations.AlterField(
            model_name='user',
            name='activation_code',
            field=models.UUIDField(blank=True, default=uuid.uuid4, null=True, verbose_name='Код активации'),
        ),
    ]