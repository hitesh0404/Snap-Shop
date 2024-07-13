# Generated by Django 5.0.6 on 2024-07-13 02:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customer_dob_customer_gender_customer_phone_number_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.BigIntegerField()),
                ('supplier_logo', models.ImageField(default='C:\\Users\\admin\\Django Project\\Main Project Folder\\media\\images\\product_image\\random_cat.jpg', upload_to='supplier/logo/')),
                ('user_create_date', models.DateTimeField(auto_now_add=True)),
                ('profile_update_date', models.DateTimeField(auto_now=True)),
                ('document_photo', models.ImageField(default='C:\\Users\\admin\\Django Project\\Main Project Folder\\media\\images\\product_image\\random_cat.jpg', upload_to='supplier/document/')),
                ('company_name', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
