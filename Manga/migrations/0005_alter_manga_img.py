# Generated by Django 5.0 on 2024-01-09 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manga', '0004_alter_manga_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='img',
            field=models.ImageField(upload_to='media/img/'),
        ),
    ]
