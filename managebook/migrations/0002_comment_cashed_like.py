# Generated by Django 3.1.1 on 2020-09-26 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managebook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='cashed_like',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
