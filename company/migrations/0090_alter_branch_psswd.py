# Generated by Django 3.2.8 on 2024-02-20 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0089_auto_20240220_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='KwMn9uwJAD', max_length=10),
        ),
    ]
