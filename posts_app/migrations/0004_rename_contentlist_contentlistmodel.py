# Generated by Django 4.2.4 on 2023-11-03 15:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts_app', '0003_alter_postmodel_user_contentlist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContentList',
            new_name='ContentListModel',
        ),
    ]
