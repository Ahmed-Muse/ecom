# Generated by Django 3.2.6 on 2021-09-20 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0059_sellingpricecalcmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellingpricecalcmodel',
            name='markup',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=2, null=True),
        ),
    ]
