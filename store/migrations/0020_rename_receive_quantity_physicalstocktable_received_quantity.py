# Generated by Django 3.2.6 on 2021-08-24 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_alter_shippingaddress_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='physicalstocktable',
            old_name='receive_quantity',
            new_name='received_quantity',
        ),
    ]
