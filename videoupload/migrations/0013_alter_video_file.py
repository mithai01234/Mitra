# Generated by Django 4.2.5 on 2023-10-27 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoupload', '0012_alter_video_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(upload_to='videos/'),
        ),
    ]