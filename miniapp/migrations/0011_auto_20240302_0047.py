# Generated by Django 3.2.19 on 2024-03-01 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniapp', '0010_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagesecond',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AddField(
            model_name='post',
            name='imagethird',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
