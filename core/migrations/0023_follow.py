# Generated by Django 4.0.5 on 2022-08-20 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_post_profileimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower_username', models.CharField(max_length=30)),
                ('following_username', models.CharField(max_length=30)),
                ('follower', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.profile')),
            ],
        ),
    ]
