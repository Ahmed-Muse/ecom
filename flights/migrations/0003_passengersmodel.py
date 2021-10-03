# Generated by Django 3.2.6 on 2021-10-03 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20211003_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassengersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=60)),
                ('lname', models.CharField(max_length=60)),
                ('flights', models.ManyToManyField(blank=True, related_name='passenger', to='flights.FlightModel')),
            ],
        ),
    ]
