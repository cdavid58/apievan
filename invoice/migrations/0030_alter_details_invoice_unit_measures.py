# Generated by Django 3.2.8 on 2024-08-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0029_details_invoice_unit_measures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details_invoice',
            name='unit_measures',
            field=models.CharField(blank=True, max_length=191, null=True),
        ),
    ]
