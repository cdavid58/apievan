# Generated by Django 3.2.8 on 2023-10-04 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_alter_branch_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='ahEu6Zidar', max_length=10),
        ),
    ]
