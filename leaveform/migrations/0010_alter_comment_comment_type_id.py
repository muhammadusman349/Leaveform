# Generated by Django 3.2.19 on 2023-07-19 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveform', '0009_alter_commentfile_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_type_id',
            field=models.IntegerField(unique=True),
        ),
    ]
