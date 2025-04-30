# filepath: c:\Users\Gustavo\Desktop\fichadetreino\fichadetreinos\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('aluno/', views.aluno, name='aluno'),
    path('treino/<int:aluno_id>/', views.treino, name='treino'),
    path('cadastrartreino/<int:aluno_id>', views.cadastrartreino, name='cadastrartreino'),
    path('cadastrarexercicio/', views.cadastrarexercicio, name='cadastrarexercicio'),
]