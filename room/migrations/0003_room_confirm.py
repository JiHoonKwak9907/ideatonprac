# Generated by Django 4.0.5 on 2022-06-30 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_rename_boby_room_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='confirm',
            field=models.ImageField(blank=True, null=True, upload_to='room_photo'),
        ),
    ]