# Generated by Django 3.2.8 on 2023-10-26 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0034_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='dgptYnMU2EHxL3CuoP28', max_length=20, unique=True),
        ),
    ]
