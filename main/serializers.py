from rest_framework import serializers
from .models import FoodCategory, Topping, Food


class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = ['cat_id', 'name', 'is_publish']


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ['top_id', 'name']


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['category_id', 'food_id', 'name', 'description',
                  'price', 'is_special', 'is_vegan', 'is_publish', 'topping']

