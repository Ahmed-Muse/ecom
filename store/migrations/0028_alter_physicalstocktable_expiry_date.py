# Generated by Django 3.2.6 on 2021-08-30 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_alter_physicalstocktable_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physicalstocktable',
            name='expiry_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
