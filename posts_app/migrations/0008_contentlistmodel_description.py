# Generated by Django 4.2.4 on 2023-11-03 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0007_rename_comments_postmodel_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentlistmodel',
            name='description',
            field=models.CharField(default='Hola', max_length=200),
            preserve_default=False,
        ),
    ]
