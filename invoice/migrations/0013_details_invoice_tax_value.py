# Generated by Django 3.2.8 on 2024-02-12 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0012_auto_20231228_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='details_invoice',
            name='tax_value',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
