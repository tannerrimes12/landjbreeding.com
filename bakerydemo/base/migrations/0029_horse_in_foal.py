# Generated by Django 2.0.7 on 2018-07-30 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_auto_20180730_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='horse',
            name='in_foal',
            field=models.NullBooleanField(help_text='Check if Horse is in foal'),
        ),
    ]
