# Generated by Django 4.2.4 on 2023-11-06 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("posts_app", "0009_alter_postmodel_content_list"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postmodel",
            name="content_list",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                to="posts_app.contentlistmodel",
            ),
        ),
    ]