# Generated by Django 3.2.8 on 2024-08-09 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0133_alter_branch_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='TYtTnXARBM', max_length=10),
        ),
    ]
