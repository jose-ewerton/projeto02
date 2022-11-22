from django.db import models

# Create your models here.

class ProdutoModel(models.Model):
     
    # fields of the model
    nome = models.CharField(max_length = 200)
    quantidade = models.IntegerField()
 
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.nome