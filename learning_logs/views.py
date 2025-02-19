from django.shortcuts import render
from .models import Topic #importa o Topic dentro do arquivo models
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect  #so exisge que se coloque uma url
from django.urls import reverse

# Create your views here.

def index(request):
    """Pafgina principal do learning_logs"""
    return render(request, "learning_logs/index.html")  

def topics(request):
    """Mostra todos os assuntos"""
    topics = Topic.objects.order_by('date_added')  #Pegando dentro da base de dados relacionado ao model Topic, e ordenar por alguma coisa
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id): #recebe dois argumentos
    """Mostra um unico assunto e todas as suas entradas."""
    topic = Topic.objects.get(id = topic_id) 
    entries = topic.entry_set.order_by('-date_added')  #ordenar de forma inversa.
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Adiciona um novo assunto."""
    if request.method != "POST":
        #Nenhum dado submetido. Cria um formulario em branco
        form = TopicForm()
    else:
        #Dados de POST submetidos. Processa os dados
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("topics"))
    
    context = {"form": form}
    return render(request, "learning_logs/new_topic.html", context)

def new_entry(request, topic_id):
    """Adiciona uma descricao"""
    topic = Topic.objects.get(id = topic_id)

    if request.method != "POST":
        #Nenhum dado submetido. Cria um formulario em branco
        form = EntryForm()  
    else: 
        #Dados de POST submetidos. Processa os dados
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, "learning_logs/new_entry.html", context)