# Generated by Django 3.2.6 on 2021-11-02 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_tasksmodel_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasksmodel',
            name='taskDay',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday')], default='Monday', max_length=200),
        ),
    ]
