# Generated by Django 3.2.6 on 2021-09-20 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0060_alter_sellingpricecalcmodel_markup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellingpricecalcmodel',
            name='markup',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]