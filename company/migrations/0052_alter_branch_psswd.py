# Generated by Django 3.2.8 on 2023-12-28 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0051_alter_branch_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='oXuFeTb7IC', max_length=10),
        ),
    ]
