from django.urls import path

from . import views


app_name="arriendos"
urlpatterns = [
    
    #ex: /clientes/
    path('', views.index, name='index'),
    #ex: /clientes/5/details
    path('dashboard/', views.dataDashboard, name='dasboard'),
    path('listado/', views.listadoMontos, name='listado'),

    # path('details/lastname', views.getClientSortByLastName, name='lastname')
] 