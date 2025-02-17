from django.db import models

# Create your models here.
#O models da-te a oprtunidade de manipular e controlar a base de dados.

class Topic(models.Model):
    """Um assunto sobre o qual o usuario esta aprendendo"""
    text = models.CharField(max_length= 200) #um atributo(campo) com nome txt do tipo texto.
    date_added = models.DateTimeField(auto_now=True)   #preencher a data, a horaque foe registada alguma coisa. Pega automaticamente a data e hora do sistema

    def __str__(self):
        """Visializar no painel adminitrativo os campos da BD. Devolve uma representacao em string do modelo."""
        return self.text
    
class Entry(models.Model):
    """Algo especifico aprendido  sobre o assunto."""
    topic = models.ForeignKey(Topic, on_delete= models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "entries" #corrigir o plural do Entry
    
    def __str__(self):
        """Devolve uma representacao em string do modelo"""
        return self.text[:50] + "..." #so vai visualizar os primeiros 50 caracteres.