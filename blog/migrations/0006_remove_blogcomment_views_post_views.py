# Generated by Django 4.1 on 2022-08-14 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogcomment_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='views',
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
