from django.db import models
from .category import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    img = models.ImageField(upload_to="Imgs")
    description = models.TextField()
    price = models.IntegerField()
    

    @staticmethod
    def get_category(get_id):
        if get_id:
            return Product.objects.filter(category=get_id)
        else:
            return Product.objects.all()
    # def __str__(self):
    #     return f"{self.name}, {self.category.name}, {self.price}"