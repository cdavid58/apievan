# Generated by Django 3.2.8 on 2024-01-02 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0056_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='OGKSbtrnz0h6JxwDXTul', max_length=20, unique=True),
        ),
    ]
