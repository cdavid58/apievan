# Generated by Django 3.2.8 on 2024-02-21 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0097_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='gGFuYfg2ZQf0BNERIrRx', max_length=20, unique=True),
        ),
    ]
