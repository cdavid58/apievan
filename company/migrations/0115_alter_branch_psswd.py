# Generated by Django 3.2.8 on 2024-03-20 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0114_alter_branch_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='9cHms1QUM1', max_length=10),
        ),
    ]
