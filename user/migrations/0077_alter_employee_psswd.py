# Generated by Django 3.2.8 on 2024-01-30 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0076_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='tvfMUoVOUPxK9nF82IHH', max_length=20, unique=True),
        ),
    ]
