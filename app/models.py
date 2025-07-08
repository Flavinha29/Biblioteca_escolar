from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class Escola(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Turma(models.Model):
    nome = models.CharField(max_length=100)
    ano_escolar = models.IntegerField(choices=[(6, "6º"), (7, "7º"), (8, "8º"), (9, "9º")])
    turno = models.CharField(max_length=20, choices=[('matutino', 'Matutino'), ('vespertino', 'Vespertino')])
    professor_responsavel = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nome} - {self.ano_escolar}º ({self.turno})"


class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    data_nasc = models.DateField()
    email = models.EmailField()
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    pontos_leitura = models.IntegerField(default=0)

    def __str__(self):
        return self.nome


class GeneroLiterario(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Gênero Literário"
        verbose_name_plural = "Gêneros Literários"


class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    genero = models.ForeignKey(GeneroLiterario, on_delete=models.CASCADE)
    faixa_etaria = models.CharField(max_length=50)
    paginas = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return self.titulo


class AvaliacaoLeitura(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    nota = models.IntegerField()
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Avaliação de {self.estudante} - {self.livro}"


class Emprestimo(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.estudante} - {self.livro}"


class RankingLeitura(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    pontos_totais = models.IntegerField()

    def __str__(self):
        return f"{self.estudante} - {self.pontos_totais} pts"


class Recompensa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='recompensas/')
    pontos_necessarios = models.IntegerField()

    def __str__(self):
        return self.nome


class DesafioLeitura(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    livros = models.ManyToManyField(Livro)
    turmas = models.ManyToManyField(Turma)

    def __str__(self):
        return self.titulo


class RelatorioDesempenho(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    desempenho = models.TextField()
    recomendacoes = models.TextField()

    def __str__(self):
        return f"Relatório de {self.estudante}"


class RecomendacaoLeitura(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    criterio = models.TextField()

    def __str__(self):
        return f"Recomendação para {self.estudante}"


class ProgressoLeitura(models.Model):
    STATUS_CHOICES = [('lendo', 'Lendo'), ('concluído', 'Concluído')]
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.estudante} - {self.livro} ({self.status})"
