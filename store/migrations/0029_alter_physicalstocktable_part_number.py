# Generated by Django 3.2.6 on 2021-08-30 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_alter_physicalstocktable_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physicalstocktable',
            name='part_number',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='part number'),
        ),
    ]
