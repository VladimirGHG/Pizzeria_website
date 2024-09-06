from django.urls import path
from . import views
app_name = 'cart'

urlpatterns = [
    path("add_cart/", views.add_cart, name="add_cart"),
    path("your_cart/", views.view_cart, name="your_cart"),
]
