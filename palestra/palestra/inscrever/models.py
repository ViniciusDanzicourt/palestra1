from django.db import models

# Create your models here.

class Palestras(models.Model):
    imagem = models.ImageField()
    nome = models.CharField(max_length=100)
    descrecao = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % (self.nome)


class Inscricao(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    palestra = models.ForeignKey(Palestras)

    def __str__(self):
        return '%s' % (self.nome)