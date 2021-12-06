# Generated by Django 3.2.9 on 2021-12-05 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0002_remove_game_players'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLoginActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_username', models.CharField(blank=True, max_length=40, null=True)),
                ('login_datetime', models.DateTimeField(auto_now=True)),
                ('logout_datetime', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
    ]
