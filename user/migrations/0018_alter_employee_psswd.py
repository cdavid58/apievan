# Generated by Django 3.2.8 on 2023-10-14 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='3ipIYnlyJZeICmI97qUK', max_length=20),
        ),
    ]
