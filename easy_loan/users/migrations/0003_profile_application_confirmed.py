# Generated by Django 3.0.9 on 2020-08-24 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='application_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]