# Generated by Django 3.2.8 on 2024-01-04 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0064_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='gdmRwQNcqsoDgwTlAqHm', max_length=20, unique=True),
        ),
    ]
