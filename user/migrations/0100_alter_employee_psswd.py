# Generated by Django 3.2.8 on 2024-02-21 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0099_auto_20240221_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='GmwAi6133Vabkk3urBN6', max_length=20, unique=True),
        ),
    ]
