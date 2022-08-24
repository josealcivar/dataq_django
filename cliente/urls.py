from django.urls import path

from . import views


app_name="clientes"
urlpatterns = [
    
    #ex: /clientes/
    path('', views.index, name='index'),
    #ex: /clientes/5/details
    path('details/', views.getClientIds, name='clientes'),

    path('details/lastname', views.getClientSortByLastName, name='lastname')
] 