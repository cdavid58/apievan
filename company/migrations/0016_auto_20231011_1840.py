# Generated by Django 3.2.8 on 2023-10-11 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0015_auto_20231011_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='If9uleuOmc', max_length=10),
        ),
        migrations.AlterField(
            model_name='resolution',
            name='date_from',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='resolution',
            name='date_to',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='resolution',
            name='generated_to_date',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='resolution',
            name='resolution',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resolution',
            name='resolution_date',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='resolution',
            name='technical_key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
