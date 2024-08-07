# Generated by Django 5.0.6 on 2024-08-06 16:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0002_order_uuid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30)),
                ('details', models.CharField(max_length=100)),
                ('discount_amount', models.PositiveIntegerField()),
                ('validity_period', models.DateField()),
                ('usage_limit', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_signature', models.CharField(default='', max_length=64)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('processing', 'processing'), ('completed', 'completed')], default='pending', max_length=20)),
                ('method', models.CharField(choices=[('RazorPay', 'RazorPay'), ('card', 'card'), ('COD', 'COD'), ('UPI', 'UPI'), ('net_banking', 'net_banking')], max_length=20)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='order.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CouponUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('used_date', models.DateTimeField(auto_now_add=True)),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.coupon')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'coupon')},
            },
        ),
    ]