# Generated by Django 3.2.8 on 2024-02-20 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0087_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='3rdaiAXCyBICuikXKq0x', max_length=20, unique=True),
        ),
    ]
