# Generated by Django 3.2.8 on 2023-12-26 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transfer',
            name='number',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]
