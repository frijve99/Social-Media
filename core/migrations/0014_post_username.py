# Generated by Django 4.0.5 on 2022-08-16 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_post_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.CharField(default='user', max_length=30),
        ),
    ]
