# Generated by Django 3.2.8 on 2024-08-09 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0010_book_account_book_account_type_transaction_types'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit_Measures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=191)),
            ],
        ),
    ]
