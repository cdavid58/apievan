# Generated by Django 3.2.8 on 2024-02-19 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_rename_shopping_report_shopping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hitory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
