from django.contrib import admin
from fichadetreinos.models import *
# Register your models here.
admin.site.site_header = "Fichas de Treinos Admin"
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Treino)
admin.site.register(Exercicio)