from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    name     = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'



class Allergen(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'allergens'


class Allergenproduct(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    allergen = models.ForeignKey('Allergen', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergensproducts'


class Image(models.Model):
    image_url = models.CharField(max_length=200)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'