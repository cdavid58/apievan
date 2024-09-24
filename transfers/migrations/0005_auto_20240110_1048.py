# Generated by Django 3.2.8 on 2024-01-10 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfers', '0004_auto_20240110_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='transfer',
            name='timestamp_returned',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.DeleteModel(
            name='Transfer_Return',
        ),
    ]
