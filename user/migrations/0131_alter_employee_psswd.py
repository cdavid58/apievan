# Generated by Django 3.2.8 on 2024-08-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0130_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='8XG0hQogATXV2gsyaJot', max_length=20, unique=True),
        ),
    ]
