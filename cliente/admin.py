from django.contrib import admin

# Register your models here.
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cliente, ClienteAdmin)