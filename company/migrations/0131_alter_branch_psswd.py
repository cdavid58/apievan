# Generated by Django 3.2.8 on 2024-08-08 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0130_alter_branch_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='YVJEVIdCtj', max_length=10),
        ),
    ]
