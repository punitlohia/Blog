# Generated by Django 2.1.5 on 2019-01-16 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
