# Generated by Django 3.2.8 on 2024-01-10 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0070_alter_branch_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='EPCccUV151', max_length=10),
        ),
    ]
