# Generated by Django 3.2.8 on 2023-10-27 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0036_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='22cLZOtnvmrNZvUQFEd5', max_length=20, unique=True),
        ),
    ]
