# Generated by Django 4.2.3 on 2023-07-22 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='service_years',
            field=models.IntegerField(default=0),
        ),
    ]
