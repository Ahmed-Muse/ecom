# Generated by Django 3.2.6 on 2021-09-04 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0036_profile_profileinterest'),
    ]

    operations = [
        migrations.CreateModel(
            name='formmodeltest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('category', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=20)),
                ('body', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='profileinterest',
            name='profile',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='ProfileInterest',
        ),
    ]