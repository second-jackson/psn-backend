# Generated by Django 4.2.4 on 2023-11-17 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts_app", "0011_remove_postmodel_content_list_postmodel_content_list"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="postmodel",
            name="content_list",
        ),
        migrations.AddField(
            model_name="contentlistmodel",
            name="posts",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                null=True,
                related_name="contents_list",
                to="posts_app.postmodel",
            ),
        ),
    ]