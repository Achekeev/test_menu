from django.shortcuts import render
import django_filters.rest_framework
from .models import FoodCategory, Topping, Food
from .serializers import FoodCategorySerializer, ToppingSerializer, FoodSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView


class FoodCategoryAPIView(CreateAPIView):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer


class ToppingAPIView(CreateAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer


class FoodAPIView(CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodCategoryListAPIView(ListAPIView):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name', 'is_publish', 'is_vegan', 'is_special']


class ToppingListAPIView(ListAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer


class FoodListAPIView(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer



class FoodCategoryDetailAPIView(RetrieveAPIView):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer


class ToppingDetailAPIView(RetrieveAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer


class FoodDetailAPIView(RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer