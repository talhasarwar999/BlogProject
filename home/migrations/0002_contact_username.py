# Generated by Django 3.1.4 on 2020-12-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='username',
            field=models.CharField(default=2, max_length=250),
            preserve_default=False,
        ),
    ]
