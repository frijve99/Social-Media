# Generated by Django 4.0.5 on 2022-07-28 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='user', max_length=100)),
                ('id_user', models.IntegerField()),
                ('firstname', models.CharField(blank=True, max_length=50)),
                ('lastname', models.CharField(blank=True, max_length=50)),
                ('phonenumber', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(blank=True, max_length=20)),
                ('dob', models.DateField(default=django.utils.timezone.now)),
                ('forget_pass_token', models.CharField(blank=True, max_length=100)),
                ('bio', models.TextField(blank=True, default='Hey its me')),
                ('profileimg', models.ImageField(default='profilepic.jpg', upload_to='profile_images')),
                ('location', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
