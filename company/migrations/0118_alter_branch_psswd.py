# Generated by Django 3.2.8 on 2024-05-06 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0117_alter_branch_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='zdj6u0g9eI', max_length=10),
        ),
    ]
