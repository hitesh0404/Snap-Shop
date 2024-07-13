# Generated by Django 5.0.6 on 2024-07-12 05:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='DOB',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='O', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.BigIntegerField(default=1234556666666),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='profile_image',
            field=models.ImageField(default='C:\\Users\\admin\\Django Project\\Main Project Folder\\media\\images\\product_image\\random_cat.jpg', upload_to='user_profile_pic/'),
        ),
        migrations.AddField(
            model_name='customer',
            name='profile_update_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='user_create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]