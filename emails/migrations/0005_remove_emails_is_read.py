# Generated by Django 3.2.8 on 2024-01-02 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0004_emails_is_read'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emails',
            name='is_read',
        ),
    ]
