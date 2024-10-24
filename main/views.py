from django.shortcuts import render
from django_filters import rest_framework as filters
from .models import Category, Topping, Food
from .serializers import FoodCategorySerializer, ToppingSerializer, FoodSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView


class FoodFilter(filters.FilterSet):
    vegan = filters.BooleanFilter(field_name='is_vegan')
    special = filters.BooleanFilter(field_name='is_special')
    publish = filters.BooleanFilter(field_name='is_publish')

    class Meta:
        model = Food
        filter_fields = ['is_vegan', 'is_special', 'is_publish']


class CategoryFilter(filters.FilterSet):
    published = filters.BooleanFilter(field_name='is_publish')

    class Meta:
        model = Category
        filter_fields = ['is_publish']


class FoodCategoryAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = FoodCategorySerializer


class ToppingAPIView(CreateAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer


class FoodAPIView(CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodCategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = FoodCategorySerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = FoodFilter, CategoryFilter


class ToppingListAPIView(ListAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer


class FoodListAPIView(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer



class FoodCategoryDetailAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = FoodCategorySerializer


class ToppingDetailAPIView(RetrieveAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer


class FoodDetailAPIView(RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer