from django.db import models
from django.contrib.auth.models import User

# modelo do aluno
class Aluno(models.Model):
    """modelo do aluno"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    peso = models.FloatField()
    altura = models.FloatField()
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em string do objeto"""
        # Devolve o nome do aluno   
        return self.nome
    
# modelo do professor
class Professor(models.Model):
    """modelo do professor"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em string do objeto"""
        # Devolve o nome do professor
        return self.nome

# modelo de exercicio
class Exercicio(models.Model):
    """modelo do exercicio"""
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    grupo_muscular = models.CharField(max_length=100)

    def __str__(self):
        """Devolve uma representação em string do objeto"""
        # Devolve o nome do exercicio
        return self.nome

# modelo de treino
class Treino(models.Model):
    """modelo do treino"""
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    ordem = models.CharField(max_length=2)
    data = models.DateField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    repeticoes = models.IntegerField()
    series = models.IntegerField()

    def __str__(self):
        """Devolve uma representação em string do objeto"""
        # Devolve o nome do treino
        return self.nome
