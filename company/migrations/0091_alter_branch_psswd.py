# Generated by Django 3.2.8 on 2024-02-20 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0090_alter_branch_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='T1Vwj07ImW', max_length=10),
        ),
    ]
