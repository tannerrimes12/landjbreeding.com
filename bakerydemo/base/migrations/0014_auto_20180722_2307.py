# Generated by Django 2.0.7 on 2018-07-22 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_auto_20180722_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horse',
            name='real_name',
        ),
        migrations.AddField(
            model_name='horse',
            name='legal_name',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]
