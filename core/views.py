from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):
    context = {
        'mensagem': "Ola mundo"
    }
    return render(request,'core/index.html', context)

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {
        'pessoas':pessoas,
        'form':form
    }
    return render (request,'core/lista_pessoas.html',data)

def pessoa_create(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_pessoas')


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {
        'veiculos':veiculos,
        'form': form
    }

    return render (request,'core/lista_veiculos.html',data)

def veiculo_create(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_veiculos')



def lista_movrotativo(request):
    movrot = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {
        'movrot': movrot,
        'form': form
    }
    return render(request,'core/lista_movrot.html',data)

def movrot_create(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_movrot')


def lista_mensalista(request):
    mensalista = Mensalista.objects.all()
    form = MensalistaForm()
    data = {
        'mensalista': mensalista,
        'form':form
    }
    return render(request,'core/lista_mensalista.html',data)

def mensalista_create(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_mensalista')



def lista_movmensalista(request):
    movmensalista = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {
        'movmensalista': movmensalista,
        'form':form
    }
    return render(request,'core/lista_movmensalista.html',data)

def movmensalista_create(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('lista_movmensalista')
