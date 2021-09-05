# Generated by Django 3.2.6 on 2021-09-04 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0039_delete_formmodeltest'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=20)),
                ('body', models.CharField(max_length=100)),
            ],
        ),
    ]
