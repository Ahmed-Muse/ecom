# Generated by Django 3.2.6 on 2021-08-27 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_auto_20210826_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physicalstocktable',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='physicalstocktable',
            name='part_number',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]