# Generated by Django 2.1.7 on 2019-03-15 19:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_auto_20190315_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoapp',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
