# Generated by Django 3.2.8 on 2023-12-29 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0052_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='fIY4zppsVlqRYzAHq0UD', max_length=20, unique=True),
        ),
    ]
