# Generated by Django 3.2.8 on 2023-12-29 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0058_alter_branch_psswd'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='value_coin',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='ZVYCKE5OFZ', max_length=10),
        ),
    ]
