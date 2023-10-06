from django.db import models
from categorias import models

# Create your models here.
class Product(models.Model):
    class Meta:
        verbose_name_plural = 'Products'
        verbose_name= 'Product'
    
    name= models.CharField(max_length=255)
    description= models.TextField()
    price= models.DecimalField(max_digits=6, decimal_places=2)
    category= models.ForeignKey('categorias.Categoria', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name} {self.price} {self.category}'