from django.db import models

# Create your models here.
class Empresa(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{} {}'.format(self.id, self.name)