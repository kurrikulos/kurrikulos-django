from django.shortcuts import render, redirect
from .models import Curriculo
from .models import Usuario
from .form import CurriculoForm
from .form import UsuarioForm


# pagina de boas vindas
def home(request):
    return render(request, 'home.html')


##########################################################
                       # USUÁRIO #
##########################################################
def login(request):
    data = {}
    form = UsuarioForm(request.POST or None)

    # validacao
    if form.is_valid():
        form.save()
        return redirect('url_criar')
    data['form'] = form
    return render(request, 'usuario/login.html', data)


##########################################################
                      # CURRÍCULO #
##########################################################

######### READ
def listagem(request):
    data = {}
    data['curriculos'] = Curriculo.objects.all()
    return render(request, 'curriculo/listagem.html', data)


######### CREATE
def criar_currilo(request):
    data = {}
    form = CurriculoForm(request.POST or None)

    # validacao
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    return render(request, 'curriculo/criar.html', data)


######### UPDATE
def atualizar_curriculo(request, pk):
    data = {}
    curriculo = Curriculo.objects.get(pk=pk)
    form = CurriculoForm(request.POST or None, instance=curriculo)

    # validacao
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    data['curriculo'] = curriculo
    return render(request, 'curriculo/atualizar.html', data)


######### DELETE
def deletar_curriculo(request, pk):
    curriculo = Curriculo.objects.get(pk=pk)
    curriculo.delete()
    return redirect('url_home')