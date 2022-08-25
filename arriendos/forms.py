from django import forms
from arriendos.models import Arriendos
from empresa.models import Empresa
from cliente.models import Cliente


class NuevoArriendo(forms.ModelForm):
    
    class Meta:
        model = Arriendos

        fields = [
            'placa',
            'marca',
            'modelo',
            'anio_vehiculo',
            'servicio',
            
        ]
        labels={
            'placa' : 'Placa:',
            'marca' : 'Marca:',
            'modelo': 'Modelo:',
            'anio_vehiculo' : 'Año:',
            'servicio' : 'servicio:',
            
        }

        widgets = {
            'placa'         : forms.TextInput(attrs={'class':'form-control'}),
            'marca'         : forms.TextInput(attrs={'class':'form-control','disabled':'True'}),
            'modelo'        : forms.TextInput(attrs={'class':'form-control','disabled':'True'}),
            'anio_vehiculo' : forms.TextInput(attrs={'class':'form-control','disabled':'True'}),
            'servicio'      : forms.TextInput(attrs={'class':'form-control','disabled':'True'}),

        }