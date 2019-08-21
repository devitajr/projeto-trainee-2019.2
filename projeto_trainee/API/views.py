from django.shortcuts import render
from qr_code.qrcode.utils import QRCodeOptions
from .models import *

context = dict(
        my_options=QRCodeOptions(size='t', border=6, error_correction='L'),
    )

# Create your views here.

def homePage(request):

    return render(request,'API/home.html')

def regras(request):

    return render(request,'API/regras.html')

def dicas(request):

    return render(request,'API/dicas.html')

def grupos(request):

    persons = Usuarios.objects.all()

    return render(request,'API/grupos.html',{'persons': persons,})

def QRcode(request):
    return render(request,'API/QRcode.html', context=context)

def documentacaoAPI(request):
    return render(request,'API/documentacao-api.html')