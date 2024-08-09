from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pizza


def home(requests):
    context = {
        'pizzas': Pizza.objects.all()
    }
    return render(requests, 'pizzas/home.html', context)


def pizza_detail(request, id):
    pizza = get_object_or_404(Pizza, id=id)
    return render(request, 'pizzas/description.html', {'pizza': pizza})

