# Generated by Django 4.2.2 on 2023-07-05 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
        ('orders', '0002_order_is_employee_order_product_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(related_name='orders', to='products.product'),
        ),
    ]
