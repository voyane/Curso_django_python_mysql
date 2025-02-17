from django.shortcuts import render

# Create your views here.

def index(request):
    """Pafgina principal do learning_logs"""
    return render(request, "learning_logs/index.html")  