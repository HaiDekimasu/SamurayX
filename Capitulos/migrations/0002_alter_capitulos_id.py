# Generated by Django 5.0 on 2024-01-06 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Capitulos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capitulos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
