# Generated by Django 2.2.1 on 2019-06-03 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchdb',
            name='distance',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='searchdb',
            name='timedata',
            field=models.DateTimeField(),
        ),
    ]
