# Generated by Django 3.2.8 on 2023-10-26 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0032_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='99YXgNvjGN0cddM7sG2u', max_length=20, unique=True),
        ),
    ]
