# Generated by Django 4.2.4 on 2023-08-06 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0008_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': 'Un usuario con esa dirreción de correo electrónico ya existe.'}, max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
