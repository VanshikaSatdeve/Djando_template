# Generated by Django 3.2.19 on 2024-02-28 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniapp', '0004_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(upload_to='images'),
        ),
    ]