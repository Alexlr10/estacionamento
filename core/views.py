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

def pessoa_update(request,id):
   pessoa = Pessoa.objects.get(id=id)
   form = PessoaForm(request.POST or None, instance= pessoa)
   data = {
       'pessoa':pessoa,
       'form':form
   }

   if request.method == 'POST':
       if form.is_valid():
           form.save()
           return redirect('lista_pessoas')
   else:
       return render(request,'core/update_pessoa.html', data)



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

def veiculo_update(request,id):
   veiculo = Veiculo.objects.get(id=id)
   form = VeiculoForm(request.POST or None, instance= veiculo)
   data = {
       'veiculo':veiculo,
       'form':form
   }

   if request.method == 'POST':
       if form.is_valid():
           form.save()
           return redirect('lista_veiculos')
   else:
       return render(request,'core/update_veiculo.html', data)


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

def movrot_update(request,id):
   movrot = MovRotativo.objects.get(id=id)
   form = MovRotativoForm(request.POST or None, instance= movrot)
   data = {
       'movrot':movrot,
       'form':form
   }

   if request.method == 'POST':
       if form.is_valid():
           form.save()
           return redirect('lista_movrot')
   else:
       return render(request,'core/update_movrot.html', data)

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

def mensalista_update(request,id):
   mensalista = Mensalista.objects.get(id=id)
   form = MensalistaForm(request.POST or None, instance= mensalista)
   data = {
       'mensalista':mensalista,
       'form':form
   }

   if request.method == 'POST':
       if form.is_valid():
           form.save()
           return redirect('lista_mensalista')
   else:
       return render(request,'core/update_mensalista.html', data)



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

def movmensalista_update(request,id):
   movmensalista = MovMensalista.objects.get(id=id)
   form = MovMensalistaForm(request.POST or None, instance= movmensalista)
   data = {
       'movmensalista':movmensalista,
       'form':form
   }

   if request.method == 'POST':
       if form.is_valid():
           form.save()
           return redirect('lista_movmensalista')
   else:
       return render(request,'core/update_movmensalista.html', data)

