# Generated by Django 3.2.6 on 2021-09-03 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0030_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='JSHtmlTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20)),
                ('quantity', models.IntegerField(default='0')),
                ('price', models.IntegerField(default='0')),
            ],
        ),
    ]