from django.shortcuts import render, get_object_or_404

from .models import Pizza


def home(requests):
    context = {
        'pizzas': Pizza.objects.all()
    }
    return render(requests, 'pizzas/home.html', context)


def pizza_detail(request, id):
    pizza = get_object_or_404(Pizza, id=id)
    return render(request, 'pizzas/description.html', {'pizza': pizza})


def about_us(request):
    return render(request, 'pizzas/about_us_page.html')


def our_products(request):
    context = {
        'pizzas': Pizza.objects.all()
    }
    return render(request, 'pizzas/all_products.html', context)
