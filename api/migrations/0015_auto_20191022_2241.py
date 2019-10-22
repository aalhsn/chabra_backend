# Generated by Django 2.2.6 on 2019-10-22 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='addresses',
            field=models.ManyToManyField(to='api.Address'),
        ),
    ]
