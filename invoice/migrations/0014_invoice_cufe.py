# Generated by Django 3.2.8 on 2024-02-12 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0013_details_invoice_tax_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='cufe',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
