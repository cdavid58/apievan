# Generated by Django 3.2.8 on 2024-02-12 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0079_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='f4b8OIoeZoGTSGeXU2ml', max_length=20, unique=True),
        ),
    ]
