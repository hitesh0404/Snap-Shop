# Generated by Django 5.0.6 on 2024-08-03 04:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0006_address_area_street_address_block_number_and_more'),
        ('product', '0006_product_brand'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(choices=[('standard', 'Standard Shipping'), ('express', 'Express Shipping'), ('overnight', 'Overnight Shipping'), ('pickup', 'In-Store Pickup'), ('courier', 'Courier Service'), ('international', 'International Shipping')], max_length=20)),
                ('charges', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('discount_percentage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('order_status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='order.orderstatus')),
                ('shipping_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='order.shipping')),
            ],
        ),
        migrations.CreateModel(
            name='Orderitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('refundable', models.BooleanField(default=True)),
                ('discount', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='order.discount')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderRefund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('reason', models.IntegerField(choices=[('1', 'Product Not Received'), ('2', 'Product Damaged'), ('3', 'Product Not as Described'), ('4', 'Other')], max_length=1)),
                ('raised_date', models.DateTimeField(auto_now_add=True)),
                ('settled_date', models.DateTimeField()),
                ('description', models.TextField()),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.orderitem')),
            ],
        ),
    ]
