# Generated by Django 5.0 on 2024-01-02 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_talk', '0016_subscriptions_delete_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='subject',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
