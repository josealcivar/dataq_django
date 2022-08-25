from django.urls import path

from . import views

app_name="empresas"
urlpatterns = [
    path('', views.index, name='index'),
    path('empresas/', views.getCompaniesSortByProfits, name='empresas'),
    path('empresas/companies', views.getCompaniesWithRentsOver1Week, name='empresas'),
]