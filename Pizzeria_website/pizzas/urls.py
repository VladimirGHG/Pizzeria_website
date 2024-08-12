from django.urls import path
from .views import home_pizzas, pizza_detail, about_us, our_products, search_pizzas, main_page
from .models import Pizza

urlpatterns = [
    path("", main_page, name='main_page'),
    path("pizzas/", home_pizzas, name='home_pizzas'),
    path('about_us/', about_us, name='about_us'),
    path('our_products/', our_products, name='all_products'),
    path('pizza/<int:id>/', pizza_detail, name='pizza_detail'),
    path('search_pizzas', search_pizzas, name='search_pizzas')
]
