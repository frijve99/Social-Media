# Generated by Django 4.0.5 on 2022-07-28 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(default='user', max_length=30),
        ),
    ]
