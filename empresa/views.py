from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum, Count, Min, Max

from .models import Empresa
from arriendos.models import Arriendos
# Create your views here.
def index(request):
    return HttpResponse("HelloWorld empresa")


'''monto totales por empresas'''
def getCompaniesSortByProfits(request):
   data= Arriendos.objects.values('empresa_id').annotate(total=Sum('costo_diario')).values('empresa_id__name','total').order_by('-total')
   print(data)
   return render(request, "funciones.html", {
    "clientes":data,
    "titulo":"listado de empresas ordenado descendiente"
   })


def getCompaniesWithRentsOver1Week(request):
    
    data= Arriendos.objects.values('empresa_id').annotate(total=Count('cliente_id')).values('empresa_id__name','total').order_by('total')
    return render(request, "funciones.html", {
    "clientes":data,
    "titulo":"listado de empresas ordenado descendiente"
    })