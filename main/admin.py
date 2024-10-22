from django.contrib import admin
from .models import FoodCategory, Food, Topping


admin.site.register(Food)
admin.site.register(FoodCategory)
admin.site.register(Topping)
