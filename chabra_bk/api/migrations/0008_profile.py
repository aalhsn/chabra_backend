# Generated by Django 2.2.6 on 2019-10-15 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0007_merge_20191014_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.PositiveIntegerField(max_length=15, null=True)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=25, null=True)),
                ('age', models.PositiveIntegerField(null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
