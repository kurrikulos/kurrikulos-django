from django.forms import ModelForm
from .models import Curriculo
from .models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'email',
            'senha'
        ]

class CurriculoForm(ModelForm):
    class Meta:
        model = Curriculo
        fields = [
            'nomeCompleto',
            'telefone',
            'idade',
            'email',
            'endereco',
            'numero',
            'ap',
            'bloco',
            'rua',
            'quadra',
            'bairro',
            'cidade',
            'estado',
            'objetivo',
            'educacao',
            'nomeCurso',
            'descricaoCurso',
            'instituicao',
            'empresa',
            'cargo',
            'periodo',
            'descricaoProfissao',
            'titulo',
            'dataExpedicao',
            'descricaoCertificado'
        ]