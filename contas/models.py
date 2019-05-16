from django.db import models

# Criando modelos
class Usuario(models.Model):
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=30)

    def __str__(self):
        return self.email

class Curriculo(models.Model):
    # dados pessoais
    nomeCompleto = models.CharField(max_length=100,)
    telefone = models.CharField(max_length=100)
    idade = models.CharField(max_length=100)
    email = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    # endereco
    endereco = models.CharField(max_length=40)
    numero = models.IntegerField(null=True,  blank=True)
    ap = models.IntegerField(null=True, blank=True)
    bloco = models.CharField(null=True,  blank=True,  max_length=8)
    rua = models.CharField(null=True,  blank=True,  max_length=10)
    quadra = models.CharField(null=True,  blank=True,  max_length=4)
    
    #localidade
    bairro = models.CharField(max_length=20)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=20)
    
    # dados profissionais
    objetivo = models.TextField()
    educacao = models.CharField(max_length=30)

    # cursos
    nomeCurso = models.CharField(null=True,  blank=True,max_length=40)
    descricaoCurso = models.TextField(null=True,  blank=True,)
    instituicao  = models.CharField(null=True,  blank=True,max_length=40)
    
    # experiencias profissionais
    empresa = models.CharField(null=True,  blank=True,  max_length=40)
    cargo = models.CharField(null=True,  blank=True,  max_length=40)
    periodo = models.DateTimeField(null=True,  blank=True)
    descricaoProfissao = models.TextField(null=True,  blank=True,)

    # certificados
    titulo = models.CharField(null=True,  blank=True,  max_length=40)
    dataExpedicao = models.DateTimeField(null=True,  blank=True,)
    descricaoCertificado = models.TextField(null=True,  blank=True,)

    class Meta:
        verbose_name_plural = 'Curriculo'
