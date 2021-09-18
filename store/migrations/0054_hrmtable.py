# Generated by Django 3.2.6 on 2021-09-18 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0053_dynamicformthreetable'),
    ]

    operations = [
        migrations.CreateModel(
            name='HRMTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_no', models.IntegerField(blank=True, default='0', null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('comment', models.CharField(blank=True, max_length=250, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
