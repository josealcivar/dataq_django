from django.db import models

# Create your models here.
class Cliente(models.Model):
    id = models.IntegerField(primary_key=True)
    rut = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)

    def __str__(self):
        return '{} {} {} {}'.format(self.id, self.rut, self.name,self.lastname)
    

