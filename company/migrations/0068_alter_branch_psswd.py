# Generated by Django 3.2.8 on 2024-01-04 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0067_alter_branch_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='GWUz0YYQtF', max_length=10),
        ),
    ]
