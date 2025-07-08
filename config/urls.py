from django.contrib import admin
from django.urls import path
from app.views import (
    IndexView,
    EstudanteListView,
    ProfessorListView,
    EscolaListView,
    TurmaListView,
    LivroListView,
    AvaliacaoListView,
    EmprestimoListView,
    RecompensaListView,
    DesafioListView,
    RankingListView,
    RecomendacaoListView,
    ProgressoListView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),

    path('estudantes/', EstudanteListView.as_view(), name='estudantes'),
    path('professores/', ProfessorListView.as_view(), name='professores'),
    path('escolas/', EscolaListView.as_view(), name='escolas'),
    path('turmas/', TurmaListView.as_view(), name='turmas'),
    path('livros/', LivroListView.as_view(), name='livros'),
    path('avaliacoes/', AvaliacaoListView.as_view(), name='avaliacoes'),
    path('emprestimos/', EmprestimoListView.as_view(), name='emprestimos'),
    path('recompensas/', RecompensaListView.as_view(), name='recompensas'),
    path('desafios/', DesafioListView.as_view(), name='desafios'),
    path('ranking/', RankingListView.as_view(), name='ranking'),
    path('recomendacoes/', RecomendacaoListView.as_view(), name='recomendacoes'),
    path('progresso/', ProgressoListView.as_view(), name='progresso'),
]
