# Generated by Django 3.2.6 on 2021-09-18 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0056_quotationtable_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwoDifferentFormsTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
