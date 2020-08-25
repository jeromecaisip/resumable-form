# Generated by Django 3.0.9 on 2020-08-24 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employment',
            name='currently_working',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='employment',
            name='end',
            field=models.DateField(blank=True, null=True),
        ),
    ]
