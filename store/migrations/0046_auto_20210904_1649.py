# Generated by Django 3.2.6 on 2021-09-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0045_profile_profileinterest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='interest',
        ),
        migrations.AddField(
            model_name='profile',
            name='interest_0',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='interest_1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='interest_2',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
