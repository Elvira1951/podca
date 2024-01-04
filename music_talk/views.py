from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from prompt_toolkit import Application
from .models import*
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import *
#from .utils import audio_to_text

def index(request):
    query = ''
    if request.GET.get('query'):
        query = request.GET.get('query')



    rows = News.objects.all().filter(title__contains=query).order_by("-created_at")
    paginator = Paginator(rows, 3)

    page_number = 1
    
    if request.GET.get('page'):
       page_number = int(request.GET.get('page'))
       print(page_number)
    print(page_number)
    print(page_number)

    
    next_page = page_number +1 if (page_number +1) <= len(paginator.page_range) else page_number
    previous_page = page_number - 1 if (page_number - 1) !=0 else page_number
 # извлечь все
# select * from News;
    latest_news = News.objects.all().first()
    top_views = News.objects.all().order_by('-counter')[:3]
    #5 отсортированных строк по убыванию
    new_news =News.objects.all().order_by("-created_at")[:3]
    users=Podcasters.objects.all()
    main_pic=MainImage.objects.first()

    context = {
        'rows': paginator.page(page_number),
        'pages': paginator.page_range,
        'latest_news':latest_news,
        'top_views': top_views,
        "next_page": next_page,
        "new_news": new_news,
        "previous_page" : previous_page,
        "users":users,
        "current_page": page_number,
        'main_pic':main_pic,
                       
    }
    context['news'] = News.objects.all()[:3] 
    context['video'] = MainVideo.objects.all()[:1][0] 
    context['newsTranscription'] = NewsTranscription.objects.all()[:3] 
    context['guests'] = Podcasters.objects.all()[:6]
     
    return render(request, 'index.html', context)
    

def audio(request):
    mp3= News.audio_file.objects.order_by('-counter')[:-1]
    context = {
        'mp3':mp3,
    }
    return render(request, 'single-post.html', context)

def SaveMessage(request):
    if request.method == "POST":
       firstname =  request.POST.get('firstname')
       lastname =  request.POST.get('lastname')
       email =  request.POST.get('email')
       message =  request.POST.get('message')
       subject = request.POST.get('subject')
       row = Contacts.objects.create(firstname=firstname,lastname=lastname,email=email,message=message,
       subject= subject)
       row.save()
       
    context={
        'news': News.objects.all()[:3],
        'video':MainVideo.objects.all()[:1][0],
    }

    return render(request,'contact.html', context)   

      
    
def about(request):
    users = Podcasters.objects.all()[:3]
    context ={
        'users':users,
    }
    context['news'] = News.objects.all()[:3]
    context['video'] = MainVideo.objects.all()[:1][0]
    return render (request, "about.html", context)    

def single_post(request, id):
    row = News.objects.get(id=id)
    Transcription = NewsTranscription.objects.filter(audioObject_id=id)
    likesCount = len( NewsLike.objects.filter(NewsObject = row) )
    row.counter = row.counter + 1
    row.save()
    context = {
        'news_list':row,
        'row':row,
        'likeCount': likesCount,
       
    } 
    context['news'] = News.objects.all()[:3] 
    return render(request, "single-post.html", context)


def upload_audio(request):
    if request.method == 'POST':
        audio_file = request.FILES['audio_file']
        new_audio = audio_file(audio_file=audio_file)
        new_audio.save()

        # Производим распознавание речи и сохраняем результат в модель
        audio_file_path = new_audio.audio_file.path
        text_result = audio_to_text(audio_file_path)
        new_audio.text_content = text_result
        new_audio.save()
    return render(request, 'single-post.html')

def DetailNews(request, id):
    row = NewsTranscription.objects.get(id=id)
    text_news = News.description.text.objects(id=id)
    author = News.author.filter(newsObject=row)
    file = News.audio_file.objects.filter(newsObject=row)
    context = {
        'row': row,
        'text_news': text_news,
        'author':author,
        'file': file,
        
    }
    return render (request, "single-post.html", context)


def like(request, id):
    id = request.GET.get('id')
    row = News.objects.get(id=id)
    row.like_count += 1
    row.save()
    return index(request)

def mp3(request):
    rows = Audio.objects.all()
    context={
        'rows': rows
    }
    return render (request, "index.html", context)

def video(request):
    rows = MainVideo.objects.all()
    context={
        'rows': rows
    }
    return render (request, "index.html", context)

def saveMail(request):
    mail = request.POST.get('mail')
    Subscriptions.objects.create(mail=mail).save()
    
    return redirect('index.html')