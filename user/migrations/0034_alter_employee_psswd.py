# Generated by Django 3.2.8 on 2023-10-26 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0033_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='apcCMMWLAlIhUjhWr1xL', max_length=20, unique=True),
        ),
    ]
