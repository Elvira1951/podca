# Generated by Django 5.0 on 2023-12-23 14:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_talk', '0006_mainnews'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainnews',
            old_name='description',
            new_name='content',
        ),
        migrations.AddField(
            model_name='mainnews',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mainnews',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
