# Generated by Django 5.0.6 on 2024-05-13 20:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pape', '0004_alter_products_categoria'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Item',
        ),
    ]
