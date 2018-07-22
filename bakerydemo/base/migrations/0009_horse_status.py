# Generated by Django 2.0.7 on 2018-07-22 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20180722_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='horse',
            name='status',
            field=models.CharField(choices=[('FS', 'For Sale'), ('S', 'Sold'), ('NFS', 'Not For Sale')], default='NFS', max_length=3),
        ),
    ]