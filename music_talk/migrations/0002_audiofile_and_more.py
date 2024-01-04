# Generated by Django 5.0 on 2023-12-18 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_talk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255)),
                ('duration_seconds', models.IntegerField()),
                ('file_audio', models.FileField(upload_to='audio/')),
            ],
        ),
        migrations.RemoveField(
            model_name='newstranscription',
            name='newsaudofileObject',
        ),
        migrations.AddField(
            model_name='newstranscription',
            name='audofileObject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='music_talk.audiofile'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='NewsAudioFile',
        ),
    ]