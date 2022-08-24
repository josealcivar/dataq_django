from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Empresa

class EmpresaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Empresa, EmpresaAdmin)