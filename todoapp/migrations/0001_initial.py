# Generated by Django 3.2.6 on 2021-10-06 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TasksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('task', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('complete', 'complete'), ('incomplete', 'incomplete')], max_length=200)),
            ],
        ),
    ]
