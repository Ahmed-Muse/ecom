# Generated by Django 3.2.6 on 2021-09-04 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0046_auto_20210904_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profileuyougsd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='interest_0',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='interest_1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='interest_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
