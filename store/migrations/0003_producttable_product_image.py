# Generated by Django 3.2.6 on 2021-08-04 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_orderitemtable_shippingaddresstable'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttable',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
