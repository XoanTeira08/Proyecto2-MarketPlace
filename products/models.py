from django.db import models
from categorias.models import Categoria
from shops.models import Shop
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    class Meta:
        verbose_name_plural = 'Products'
        verbose_name= 'Product'
    
    name= models.CharField(max_length=255)
    description= models.TextField()
    slug= models.SlugField(max_length=50, blank=True, null=True,unique=True)
    price= models.DecimalField(max_digits=6, decimal_places=2)
    category= models.ForeignKey('categorias.Categoria', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='products/', blank=True, null=True)
    shop= models.ForeignKey('shops.Shop', on_delete=models.SET_NULL, null=True)

    def save (self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.name} {self.price} {self.category}'
    

class Reviews(models.Model):
    class Meta:
        verbose_name_plural = 'Reviews'
        verbose_name= 'Review'
    

    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    review= models.TextField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    score= models.IntegerField()

    # def save (self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = slugify(self.name)
    #     super(Reviews, self).save(*args, **kwargs)


    def __str__(self) -> str:
        return f' {self.review} {self.created_at} {self.score} {self.product}'