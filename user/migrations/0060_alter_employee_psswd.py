# Generated by Django 3.2.8 on 2024-01-02 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0059_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='zBNhXWUj7I4RXwSbKAib', max_length=20, unique=True),
        ),
    ]
