# Generated by Django 2.0.7 on 2018-07-30 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_horse_stud_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horse',
            name='stud_service',
            field=models.BooleanField(default=False, verbose_name=django.db.models.deletion.SET_DEFAULT),
        ),
    ]
