import datetime
from django.shortcuts import render, redirect
from .models import Aluno, Professor, Treino, Exercicio
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    """View para a página inicial."""
    alunos = Aluno.objects.all()
    professores = Professor.objects.all()
    return render(request, 'home.html', {'alunos': alunos, 'professores': professores})

def login(request):
    """View para a página de login."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                # Lógica para autenticar o usuário
                #se usuario for professor redirecionar para home
                if hasattr(user, 'professor'):
                    return redirect('home')
                #se usuario for aluno redirecionar para treino
                elif hasattr(user, 'aluno'):
                    aluno = Aluno.objects.get(user=user)
                    return redirect('treino', aluno_id=aluno.id)
            else:
                # Lógica para lidar com senha incorreta
                return render(request, 'login.html', {'error': 'Senha incorreta'})
        except User.DoesNotExist:
            # Lógica para lidar com usuário não encontrado
            return render(request, 'login.html', {'error': 'Usuário não encontrado'})
    return render(request, 'login.html')

def logout(request):
    """View para a página de logout."""
    return render(request, 'logout.html')

def cadastro(request):
    """View para a página de cadastro."""
    return render(request, 'cadastro.html')

def aluno(request, aluno_id):
    """View para a página de detalhes do aluno."""
    aluno = Aluno.objects.get(id=aluno_id)
    treinos = Treino.objects.filter(aluno=aluno)
    return render(request, 'aluno.html', {'aluno': aluno, 'treinos': treinos})

def professor(request):
    """View para a página de detalhes do professor."""
    professores = Professor.objects.all()
    return render(request, 'professor.html', {'professores': professores})

def treino(request,aluno_id):
    """View para a página de detalhes do treino."""
    aluno = Aluno.objects.get(id=aluno_id)
    # Verifica se o usuário logado é o mesmo que está acessando a página
    treinos = Treino.objects.filter(aluno=aluno).order_by('ordem')
    return render(request, 'treino.html', {'aluno':aluno, 'treinos': treinos})
@login_required
def cadastrartreino(request, aluno_id):
    """View para a página de cadastro de treino."""
    aluno = get_object_or_404(Aluno, id=aluno_id)
    exercicios = Exercicio.objects.all()
    if request.method == 'POST':
        try:
            exercicio_nome = request.POST['exercicio']
            nome = request.POST['nome']
            descricao = request.POST['descricao']
            ordem = request.POST['ordem']
            repeticoes = request.POST['repeticoes']
            series = request.POST['series']
            exercicio = Exercicio.objects.get(nome=exercicio_nome)
            professor = request.user.professor
            Treino.objects.create(
                aluno=aluno,
                exercicio=exercicio,
                nome=nome,
                descricao=descricao,
                ordem=ordem,
                data=datetime.datetime.now(),
                professor=professor,
                repeticoes=repeticoes,
                series=series
            )
            pass
        except Exception as e:
            # Lógica para lidar com erros
            print(f"Erro ao cadastrar treino: {e}")
            return render(request, 'cadastrartreino.html', {'error': str(e), aluno: aluno, 'exercicios': exercicios})
    return render(request, 'cadastrartreino.html', {'aluno': aluno, 'exercicios': exercicios})

def excluirtreino(request, treino_id):
    """View para excluir um treino."""
    treino = Treino.objects.get(id=treino_id)
    if request.method == 'POST':
        treino.delete()
        return redirect('treino')
    return render(request, 'excluirtreino.html', {'treino': treino})

def cadastrarexercicio(request):
    """View para a página de cadastro de exercício."""
    if request.method == 'POST':
        try:
            nome = request.POST['nome']
            descricao = request.POST['descricao']
            grupo_muscular = request.POST['grupo_muscular']
            # Lógica para cadastrar o exercício
            exercicio = Exercicio(nome=nome, descricao=descricao, grupo_muscular=grupo_muscular)
            exercicio.save()
            return redirect('home')
        except Exception as e:
            # Lógica para lidar com erros
            print(f"Erro ao cadastrar exercício: {e}")
            return render(request, 'cadastrarexercicio.html', {'error': str(e)})    
    return render(request, 'cadastrarexercicio.html')