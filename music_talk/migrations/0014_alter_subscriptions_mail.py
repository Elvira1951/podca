# Generated by Django 5.0 on 2024-01-01 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_talk', '0013_alter_subscriptions_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptions',
            name='mail',
            field=models.TextField(max_length=250),
        ),
    ]
