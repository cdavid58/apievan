# Generated by Django 3.2.8 on 2023-10-14 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='z7WTmzCjhVwG35saZ87k', max_length=20),
        ),
    ]
