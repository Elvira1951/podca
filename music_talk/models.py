from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone






# Create your models here.
class Podcast(models.Model):
    title = models.CharField(max_length=250,verbose_name="Theme")

    def __str__(self):
        return f'{self.title}'
    
class MainImage(models.Model):
    image = models.ImageField()

class Podcasters(models.Model):
    fillname =models.CharField(max_length=250)
    avatar = models.ImageField()
    status = models.CharField(max_length=250)
    description = models.TextField()

class Guests(models.Model):
    podcastersObject = models.ForeignKey(Podcasters, on_delete=models.CASCADE)    

class Contacts(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    message = models.CharField(max_length=250)
    subject= models.CharField(max_length=250)
    

    def get_absolute_url(self):
        return reverse('index') 
       
class News(models.Model):
    title = models.CharField(max_length=250, verbose_name="Тема новостей")
    description = models.TextField()
    news_image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор")
    audio_file = models.FileField(upload_to='audio/')
    counter = models.IntegerField(editable=False, default=0, blank=True,null=True)
    like_count = models.IntegerField(editable=False, default=0, blank=True,null=True)
    
class Audio(models.Model):
    filename = models.CharField(max_length=255)
    duration_seconds = models.IntegerField()
    last_file= models.FileField(upload_to='audio/')
    text_content = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.filename
    
class Subscriptions(models.Model):
    mail = models.TextField(max_length=250)
    
class NewsTranscription(models.Model):
    image = models.ImageField() 
    title = models.CharField(News,max_length=240)
    text = models.TextField()
    audioObject_id = models.ForeignKey(Audio, on_delete=models.CASCADE)
    text_content = models.TextField(blank=True, null=True)

class NewsLike(models.Model):
    NewsObject = models.ForeignKey(News, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    ) 

class MainVideo(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    video_image = models.ImageField(upload_to='videosImages/') 