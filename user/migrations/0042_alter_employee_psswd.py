# Generated by Django 3.2.8 on 2023-12-26 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0041_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='n97uPjtEDdtzCeX9QtPu', max_length=20, unique=True),
        ),
    ]
