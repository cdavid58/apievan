# Generated by Django 3.2.8 on 2023-10-14 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0023_alter_branch_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='EfMCdPfIjO', max_length=10),
        ),
    ]
