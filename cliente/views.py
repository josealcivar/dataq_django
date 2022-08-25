from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Cliente
# Create your views here.
def index(request):
    return HttpResponse("HelloWorld Cliente")

def details(request, question_id):
    return HttpResponse(f"estas viendo la {question_id}")

def result(request, question_id):
    return HttpResponse(f"estas viendo el resultado del {question_id}")

'''
Obtener lista con los clientes.
'''
# retorna una lista de IDS de clientes
def getClientIds(request):
    clientes = Cliente.objects.all()
    return render(request, "funciones.html", {
        "clientes": clientes,
        "titulo":"lista de clientes"
    })


'''
Obtener lista con los ids de clientes ordenados por apellidos.
'''
def getClientSortByLastName(request):
    ids_clientes = Cliente.objects.all().order_by('lastname')
    return render(request, "funciones.html", {
        "clientes": ids_clientes,
        "titulo":"clientes ordenados por Apellidos"
    })

