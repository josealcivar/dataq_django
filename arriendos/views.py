from http.client import HTTPResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Sum, Count, Min, Max
from django.db.models.functions import TruncMonth
from rest_framework import status
from statistics import mean
import datetime 

from django.core import serializers
import json 

from .models import Arriendos
from cliente.models import Cliente
# Create your views here.


def index(request):
    return HTTPResponse("HelloWorld Arriendos")

def getDashboard(request):
    # clientes = Cliente.objects.all()
    getClienteMenorMonto()
    return render(request, "dashboard.html", {
       
    })

def getArriendoTotalCliente():
    data=Arriendos.objects.all().filter('cliente').aggregate(total=Sum('costo_diario'))
    print(data)
    
''' total arriendo del mes'''
def getResumenMensual():
    # data=Arriendos.objects.all().filter('cliente').aggregate(total=Sum('costo_diario'))
    return Arriendos.objects.all().annotate(month=TruncMonth('fecha_arriendo')).values('month').annotate(total=Sum('costo_diario')).order_by()
    #return #Arriendos.objects.values('cliente_id').annotate(total=Sum('costo_diario')).values('cliente_id__name','cliente_id__lastname','total').order_by('total')
    
    
'''monto totales por empresas'''
def getMontoEmpresa():
    return Arriendos.objects.values('empresa_id').annotate(total=Sum('costo_diario')).values('empresa_id__name','total').order_by('total')


''' lista de clientes''' 
def getMontosClientes():
    return Arriendos.objects.values('cliente_id').annotate(total=Sum('costo_diario')).values('cliente_id__name','cliente_id__lastname','total').order_by('total')

def getClienteMenorMonto():
    cliente = Arriendos.objects.values_list('cliente_id','costo_diario')
    cliente2 = Arriendos.objects.values('cliente_id').annotate(total=Sum('costo_diario')).values('cliente_id__name','cliente_id__lastname','total').order_by('total')
    print(cliente2)
    minimo = cliente.order_by('costo_diario').first()
    print(minimo[0])


def dataDashboard(request, queryset=None):
    # cliente = Arriendos.objects.values_list('cliente_id','costo_diario')
    empresas = Arriendos.objects.values('empresa_id').annotate(total=Sum('costo_diario')).values('empresa_id__name','total').order_by('total')
    # print(cliente2)
    data=[]
    labels=[]
    labels_empresas=[]
    data_empresas=[]
    for emp in empresas:
        labels_empresas.append(emp['empresa_id__name'])
        data_empresas.append(emp['total'])
    datos=getResumenMensual()
    for entry in datos:
        mes=datetime.datetime.strftime(entry['month'],"%b")
        labels.append(mes)
        data.append(entry['total'])
    maximo_monto_mes=max(data)
    promedio_monto_mes=mean(data)
    print(empresas)
    cliente_monimo = (getMontosClientes()[0])
    cliente_maximo = (list(getMontosClientes())[-1])
    print(cliente_maximo)
    return render(request, "dashboard.html", {
       'clientes': empresas,
       'datos_mensuales':data,
       'labels_meses':labels,
       'empresas':empresas,
       'labels_empresas':labels_empresas,
       'promedio_monto_mes':promedio_monto_mes,
       'monto_empresas':data_empresas,
       'max_monto_mes':maximo_monto_mes,
       'cliente_min':cliente_monimo,
       'cliente_maximo':cliente_maximo
    })


def listadoMontos():
    pass