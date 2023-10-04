from django.db import models
from django.utils.text import slugify

# Create your models here.
class Categoria(models.Model):
    class Meta:
        verbose_name_plural = 'Categorias'
        verbose_name= 'Categoria'

    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    imagen = models.ImageField(upload_to='categorias', blank=True, null=True)

    def save (self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nombre)
        super(Categoria, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.nombre
