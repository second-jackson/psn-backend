# Generated by Django 4.2.4 on 2023-11-03 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0004_rename_contentlist_contentlistmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentlistmodel',
            name='posts',
        ),
        migrations.AddField(
            model_name='postmodel',
            name='content_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_list', to='posts_app.contentlistmodel'),
        ),
    ]
