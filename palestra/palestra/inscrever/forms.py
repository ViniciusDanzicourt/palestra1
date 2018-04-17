# -*- coding: utf 8 -*-
from django import forms
from models import *

class PalestraForm(forms.ModelForm):
    class Meta:
        model = Palestras
        fields = ('imagem', 'nome','descrecao')


class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ('nome', 'telefone','email','palestra')


