# Generated by Django 4.2.4 on 2023-11-03 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0006_rename_messages_postmodel_comments_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postmodel',
            old_name='comments',
            new_name='messages',
        ),
    ]