# Generated by Django 3.2.19 on 2023-07-19 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20230719_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='employee_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
