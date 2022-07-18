from tabnanny import verbose
from django.db import models                           
from django.contrib.auth.models import User

class Sellers(models.Model):
    name = models.CharField("Имя", max_length=20, unique=True, blank=True)
    ogrn = models.IntegerField("ОГРН", unique=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Продавец"
        verbose_name_plural = "Продавцы"

class Products(models.Model):
    code = models.IntegerField("Код", blank=True)
    name = models.CharField("Имя", max_length=50, blank=True)
    seller = models.ForeignKey('Sellers', on_delete=models.CASCADE, verbose_name="Продавец")
    color = models.CharField("Цвет", max_length=20, blank=True)
    price = models.IntegerField("Цена", blank=True)
    img = models.ImageField("Изображение-1", upload_to='product_img/', blank=True)
    img_1 = models.ImageField("Изображение-2", upload_to='product_img/', blank=True)
    favorite = models.ManyToManyField(User, blank=True, related_name="user_favorite", verbose_name="Избранное")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"