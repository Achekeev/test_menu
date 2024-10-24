from rest_framework import serializers
from .models import Category, Topping, Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['category', 'id', 'name', 'description',
                  'price', 'is_special', 'is_vegan', 'is_publish', 'topping']


class FoodCategorySerializer(serializers.ModelSerializer):
    foods = FoodSerializer(source='food_categories', many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'is_publish', 'foods']


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ['id', 'name']




