from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)
    is_publish = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='food_categories')
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()
    is_special = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_publish = models.BooleanField(default=False)
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name='toppings')

    def __str__(self):
        return self.name

