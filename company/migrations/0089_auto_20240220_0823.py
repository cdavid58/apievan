# Generated by Django 3.2.8 on 2024-02-20 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0088_alter_branch_psswd'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='ping',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='IMYHiX0tT7', max_length=10),
        ),
    ]
