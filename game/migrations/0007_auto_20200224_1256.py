# Generated by Django 2.2.5 on 2020-02-24 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20200224_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='name',
        ),
        migrations.AddField(
            model_name='building',
            name='tittle',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
