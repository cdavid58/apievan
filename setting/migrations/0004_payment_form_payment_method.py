# Generated by Django 3.2.8 on 2023-10-10 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0003_auto_20231004_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment_Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Payment_Method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
