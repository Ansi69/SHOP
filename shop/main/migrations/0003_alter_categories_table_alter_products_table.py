# Generated by Django 5.1.1 on 2024-09-20 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_categories_alter_products_product_name'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='categories',
            table='Категория',
        ),
        migrations.AlterModelTable(
            name='products',
            table='Товар',
        ),
    ]