# Generated by Django 3.2.8 on 2024-02-21 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0091_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='PX0EzR6oXTQGjzIMFIDD', max_length=20, unique=True),
        ),
    ]
