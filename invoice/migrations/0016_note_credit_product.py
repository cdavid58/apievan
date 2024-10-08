# Generated by Django 3.2.8 on 2024-02-26 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0103_auto_20240226_1555'),
        ('invoice', '0015_invoice_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note_Credit_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=150)),
                ('quantity', models.IntegerField()),
                ('tax', models.FloatField()),
                ('cost', models.FloatField()),
                ('price', models.FloatField()),
                ('ipo', models.FloatField()),
                ('discount', models.FloatField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.employee')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.invoice')),
            ],
        ),
    ]
