# Generated by Django 2.1.5 on 2019-01-17 18:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190117_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='users',
        ),
        migrations.AlterField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='Followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='Following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]