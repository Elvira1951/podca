# Generated by Django 5.0 on 2023-12-21 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_talk', '0003_rename_audiofile_audio_rename_file_audio_audio_file_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newstranscription',
            name='newsObject',
        ),
        migrations.AddField(
            model_name='newstranscription',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='NewsImages',
        ),
    ]