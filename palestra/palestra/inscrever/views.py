# -*- coding: utf 8 -*-
from django.shortcuts import render
from forms import *
from models import *
# Create your views here.

def Cadastro (request):
    palestras = Palestras.objects.all()
    if request.method == 'POST':
        form = InscricaoForm(request.POST)
        if form.is_valid():
            inscricao = form.save(commit=False)
            inscricao.save()
            print 'Salvo'
            
            return render(request, 'index.html', {'pales': palestras})
        else:
            print form.errors
    form = InscricaoForm()

    return render(request, 'index.html', {'pales': palestras, 'form':form})
