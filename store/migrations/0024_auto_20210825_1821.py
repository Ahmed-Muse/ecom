# Generated by Django 3.2.6 on 2021-08-25 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_alter_physicalstocktable_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physicalstocktable',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='physicalstocktable',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='physicalstocktable',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
