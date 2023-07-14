# Generated by Django 3.2.19 on 2023-07-13 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveform', '0004_auto_20230712_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_id',
            new_name='comment_type_id',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_type',
            field=models.CharField(choices=[('Leave', 'Leave'), ('TimeLog', 'TimeLog')], max_length=120),
        ),
        migrations.AlterField(
            model_name='commentfile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='Comment_File/'),
        ),
    ]
