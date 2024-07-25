# Generated by Django 5.0.6 on 2024-07-25 06:20

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='media\\banner-01.jpg', upload_to='carousel/')),
                ('title', ckeditor.fields.RichTextField()),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
