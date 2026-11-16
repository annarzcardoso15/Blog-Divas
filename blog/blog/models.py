from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_post = models.DateTimeField(default=timezone.now)
    categorias = models.ManyToManyField(Category, related_name='posts', blank=True) 

    def __str__(self):
        return self.titulo

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_postagem']

    def __str__(self):
        return f'Comentário de {self.autor.username}'