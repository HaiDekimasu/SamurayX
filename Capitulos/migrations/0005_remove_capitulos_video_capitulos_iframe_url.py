# Generated by Django 5.0 on 2024-01-14 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Capitulos', '0004_alter_capitulos_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capitulos',
            name='video',
        ),
        migrations.AddField(
            model_name='capitulos',
            name='iframe_url',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
