# Generated by Django 3.2.8 on 2023-10-14 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='dv',
            field=models.IntegerField(default=0),
        ),
    ]
