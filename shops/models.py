from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.
class Shop(models.Model):
    class Meta:
        verbose_name_plural = 'Shops'
        verbose_name= 'Shop'

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    score = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='shops/', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    def save (self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Shop, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name    
    
class ReviewShop(models.Model):
    class Meta:
        verbose_name_plural = 'ReviewsShop'
        verbose_name= 'ReviewShop'
    

    shop= models.ForeignKey(Shop, on_delete=models.CASCADE)
    review= models.TextField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    score= models.IntegerField()


    def __str__(self) -> str:
        return f' {self.review} {self.created_at} {self.score} {self.shop}'
