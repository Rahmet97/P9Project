# Generated by Django 4.2 on 2023-05-04 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_product_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(null=True),
        ),
    ]
