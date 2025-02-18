from django.shortcuts import render
from .models import Topic #importa o Topic dentro do arquivo models

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