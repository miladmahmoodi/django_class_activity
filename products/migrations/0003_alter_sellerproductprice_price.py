# Generated by Django 4.2.1 on 2023-06-08 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_image_alter_productoption_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerproductprice',
            name='price',
            field=models.PositiveSmallIntegerField(verbose_name='price'),
        ),
    ]