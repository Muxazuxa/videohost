# Generated by Django 2.1.4 on 2018-12-18 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0004_userprofile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
    ]
