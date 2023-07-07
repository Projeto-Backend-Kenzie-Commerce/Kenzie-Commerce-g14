# Generated by Django 4.2.2 on 2023-07-07 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop_cart', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='shop_cart', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cartproduct',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_cart.shopcart'),
        ),
        migrations.AddField(
            model_name='cartproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
