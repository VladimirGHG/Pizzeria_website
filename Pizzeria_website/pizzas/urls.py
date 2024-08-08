from django.urls import path
from .views import home, pizza_detail
from .models import Pizza

urlpatterns = [
    path("", home, name="home"),
    path('pizza/<int:id>/', pizza_detail, name='pizza_detail'),
]
