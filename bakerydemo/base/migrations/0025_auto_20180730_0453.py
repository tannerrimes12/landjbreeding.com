# Generated by Django 2.0.7 on 2018-07-30 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_auto_20180729_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horse',
            old_name='legal_name',
            new_name='registered_name',
        ),
    ]
