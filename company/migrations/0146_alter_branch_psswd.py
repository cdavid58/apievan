# Generated by Django 3.2.8 on 2024-09-24 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0145_auto_20240924_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='LVxZbHVvrx', max_length=30),
        ),
    ]
