# Generated by Django 3.2.8 on 2024-02-21 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0003_alter_payroll_data_payroll'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='annulled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='payroll',
            name='cune',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
