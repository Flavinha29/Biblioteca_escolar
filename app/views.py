from django.views.generic import ListView, View
from django.shortcuts import render
from .models import (
    Estudante, Professor, Escola, Turma, Livro,
    AvaliacaoLeitura, Emprestimo, Recompensa,
    DesafioLeitura, RankingLeitura, RecomendacaoLeitura,
    ProgressoLeitura
)

# Página inicial
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


# Views de listagem
class EstudanteListView(ListView):
    model = Estudante
    template_name = 'estudantes.html'
    context_object_name = 'estudantes'


class ProfessorListView(ListView):
    model = Professor
    template_name = 'professores.html'
    context_object_name = 'professores'


class EscolaListView(ListView):
    model = Escola
    template_name = 'escolas.html'
    context_object_name = 'escolas'


class TurmaListView(ListView):
    model = Turma
    template_name = 'turmas.html'
    context_object_name = 'turmas'


class LivroListView(ListView):
    model = Livro
    template_name = 'livros.html'
    context_object_name = 'livros'


class AvaliacaoListView(ListView):
    model = AvaliacaoLeitura
    template_name = 'avaliacoes.html'
    context_object_name = 'avaliacoes'


class EmprestimoListView(ListView):
    model = Emprestimo
    template_name = 'emprestimos.html'
    context_object_name = 'emprestimos'


class RecompensaListView(ListView):
    model = Recompensa
    template_name = 'recompensas.html'
    context_object_name = 'recompensas'


class DesafioListView(ListView):
    model = DesafioLeitura
    template_name = 'desafios.html'
    context_object_name = 'desafios'


class RankingListView(ListView):
    model = RankingLeitura
    template_name = 'ranking.html'
    context_object_name = 'ranking'


class RecomendacaoListView(ListView):
    model = RecomendacaoLeitura
    template_name = 'recomendacoes.html'
    context_object_name = 'recomendacoes'


class ProgressoListView(ListView):
    model = ProgressoLeitura
    template_name = 'progresso.html'
    context_object_name = 'progresso'
