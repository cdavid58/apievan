# Generated by Django 3.2.8 on 2023-10-10 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_alter_branch_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='pwyIKYpThE', max_length=10),
        ),
    ]
