# Generated by Django 3.2.8 on 2024-05-06 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0113_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='DuGQli0T6KvPfMXmMMUt', max_length=20, unique=True),
        ),
    ]
