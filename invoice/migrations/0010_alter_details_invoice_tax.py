# Generated by Django 3.2.8 on 2023-10-27 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0009_history_invoice_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details_invoice',
            name='tax',
            field=models.FloatField(),
        ),
    ]
