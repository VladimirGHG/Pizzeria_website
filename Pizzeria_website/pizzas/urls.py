from django.urls import path

from .views import home_pizzas, pizza_detail, about_us, our_products, search_pizzas, main_page, home_burgers, \
    burger_detail, restaurant_detail, home_restaurants, create_product, update_burger, add_restaurant, update_pizza, \
    delete_restaurant

urlpatterns = [
    path("", main_page, name='main_page'),
    path('pizzas/', home_pizzas, name='home_pizzas'),
    path('about_us/', about_us, name='about_us'),
    path('our_products/', our_products, name='all_products'),
    path('pizza/<int:id>/', pizza_detail, name='pizza_detail'),
    path('search_pizzas', search_pizzas, name='search_pizzas'),
    path('burgers/', home_burgers, name='home_burgers'),
    path('burger/<int:id>/', burger_detail, name='burger_detail'),
    path('restaurants/', home_restaurants, name='home_restaurants'),
    path('restaurant/<int:id>', restaurant_detail, name='restaurant_detail'),
    path('create_product/', create_product, name='create_product'),
    path('burger/update/<int:burger_id>/', update_burger, name='update_burger'),
    path('pizza/update/<int:pizza_id>/', update_pizza, name='update_pizza'),
    path('add_restaurant/', add_restaurant, name='add_restaurant'),
    path('delete_restaurant/<int:restaurant_id>', delete_restaurant, name='delete_restaurant'),
]
