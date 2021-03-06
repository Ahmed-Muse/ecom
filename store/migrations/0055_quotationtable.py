# Generated by Django 3.2.6 on 2021-09-18 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0054_hrmtable'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuotationTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('unit_price', models.IntegerField(null=True)),
                ('total_price', models.IntegerField(null=True)),
            ],
        ),
    ]
