# Generated by Django 3.2.8 on 2024-05-08 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0120_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='yzfaLzUOmMyNCQdQWIq5', max_length=20, unique=True),
        ),
    ]
