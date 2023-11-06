# Generated by Django 4.2.4 on 2023-10-29 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewspaperModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, null=True, upload_to='newspaper')),
                ('text', models.TextField()),
            ],
        ),
    ]