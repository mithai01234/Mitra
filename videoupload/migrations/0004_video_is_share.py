# Generated by Django 4.2.5 on 2023-10-18 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoupload', '0003_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='is_share',
            field=models.BooleanField(default=False),
        ),
    ]
