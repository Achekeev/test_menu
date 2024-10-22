from django.db import models


class FoodCategory(models.Model):
    cat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    is_publish = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Topping(models.Model):
    top_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Food(models.Model):
    category_id = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    food_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()
    is_special = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_publish = models.BooleanField(default=False)
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

