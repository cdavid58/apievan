# Generated by Django 3.2.8 on 2023-10-04 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='f5yQnAMx5i', max_length=10),
        ),
    ]
