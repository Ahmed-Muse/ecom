# Generated by Django 3.2.6 on 2021-08-24 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20210824_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForTey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, null=True)),
                ('product_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('product_price', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
