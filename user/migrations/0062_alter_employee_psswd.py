# Generated by Django 3.2.8 on 2024-01-02 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0061_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='qcYr4hNYJvi4IRd5aFbg', max_length=20, unique=True),
        ),
    ]
