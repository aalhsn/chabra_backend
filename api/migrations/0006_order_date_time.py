# Generated by Django 2.2.6 on 2019-10-20 07:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_order_order_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]