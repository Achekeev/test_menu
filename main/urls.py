from django.urls import path
from .views import FoodAPIView, FoodCategoryAPIView, ToppingAPIView, FoodListAPIView, FoodCategoryListAPIView, \
    ToppingListAPIView, FoodDetailAPIView, FoodCategoryDetailAPIView, ToppingDetailAPIView


urlpatterns = [
    path('category_create/', FoodCategoryAPIView.as_view(), name='Category_Create'),
    path('topping_create/', ToppingAPIView.as_view(), name='topping_create'),
    path('food_create/', FoodAPIView.as_view(), name='food_create'),
    path('category_list/', FoodCategoryListAPIView.as_view(), name='Categories_list'),
    path('topping_list/', ToppingListAPIView.as_view(), name='topping_list'),
    path('food_list/', FoodListAPIView.as_view(), name='food_list'),
    path('category_detail/<int:pk>/', FoodCategoryDetailAPIView.as_view(), name='Category_details'),
    path('topping_detail/<int:pk>/', ToppingDetailAPIView.as_view(), name='topping_details'),
    path('food_detail/<int:pk>/', FoodDetailAPIView.as_view(), name='food_details'),
]