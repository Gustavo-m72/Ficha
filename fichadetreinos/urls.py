# filepath: c:\Users\Gustavo\Desktop\fichadetreino\fichadetreinos\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('treino/<int:aluno_id>/', views.treino, name='treino'),
    path('cadastrartreino/<int:aluno_id>/', views.cadastrartreino, name='cadastrartreino'),
    path('cadastrarexercicio/', views.cadastrarexercicio, name='cadastrarexercicio'),
]