# Generated by Django 3.2.8 on 2024-03-20 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0110_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='JtJdZPA5g6BYeomhIrgG', max_length=20, unique=True),
        ),
    ]
