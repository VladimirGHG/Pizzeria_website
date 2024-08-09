from django.urls import path
from .views import home, pizza_detail, about_us, our_products
from .models import Pizza

urlpatterns = [
    path("", home, name="home"),
    path('about_us/', about_us, name='about_us'),
    path('our_products/', our_products, name='all_products'),
    path('pizza/<int:id>/', pizza_detail, name='pizza_detail'),
]
