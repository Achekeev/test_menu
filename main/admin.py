from django.contrib import admin
from .models import Category, Food, Topping


admin.site.register(Food)
admin.site.register(Category)
admin.site.register(Topping)
