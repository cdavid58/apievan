# Generated by Django 3.2.8 on 2024-01-12 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0069_alter_employee_psswd'),
        ('payroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.employee'),
        ),
    ]
