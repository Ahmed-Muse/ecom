# Generated by Django 3.2.6 on 2021-09-20 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0058_quotationcustomertable'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellingPriceCalcModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, null=True)),
                ('product_cost', models.IntegerField(blank=True, default=0, null=True)),
                ('markup', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]