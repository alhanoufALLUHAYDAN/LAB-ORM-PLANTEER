from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=255)
    alpha_code = models.CharField(max_length=2)
    def __str__(self):
        return self.name

class Plant(models.Model):

    class Category(models.TextChoices):

        FLOWER = 'flower','Flower'
        TREE = 'tree', 'Tree'
        HERB = 'herb', 'Herb'
        SHRUBS = 'shrubs' , 'Shrubs'
        AQUATIC = 'aquatic' , 'Aquatic Plant'
        FUNGUS = 'fungus' , 'Fungus'
        SHADOW = 'shadow', 'Shadow Plant'
        FRUIT = 'fruit' , 'Fruit'
        VEGETABLE = 'vegetable', 'Vegetable'
        
    title = models.CharField(max_length=1024)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="images/",default="images/default.JPG")
    category = models.CharField(max_length=10, choices=Category.choices)
    is_edible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    native_to = models.ManyToManyField(Country)

