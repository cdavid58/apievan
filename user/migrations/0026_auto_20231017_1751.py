# Generated by Django 3.2.8 on 2023-10-17 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='iWmenhfWXTGosXFO8VZW', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='user_name',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
