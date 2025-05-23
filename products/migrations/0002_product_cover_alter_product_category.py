# Generated by Django 5.1.7 on 2025-03-29 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cover',
            field=models.ImageField(blank=True, default='', upload_to='products/covers/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category'),
        ),
    ]
