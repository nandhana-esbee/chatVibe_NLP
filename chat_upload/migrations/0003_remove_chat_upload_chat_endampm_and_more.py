# Generated by Django 5.0.2 on 2024-03-24 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_upload', '0002_remove_chat_upload_chat_enddatetime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat_upload',
            name='chat_endampm',
        ),
        migrations.RemoveField(
            model_name='chat_upload',
            name='chat_startampm',
        ),
    ]
