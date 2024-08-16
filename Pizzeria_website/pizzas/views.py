from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Pizza, Burger, Restaurants


def home_pizzas(requests):
    context = Pizza.objects.all()
    paginator = Paginator(context, 6)  # Show 6 pizzas per page.

    page_number = requests.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(requests, 'pizzas/products_home.html', {'products': context, 'page_obj': page_obj, 'pr': 'pizza'})


def pizza_detail(request, id):
    pizzas = Pizza.objects.all()
    pizza = get_object_or_404(Pizza, id=id)
    restaurants = pizza.restaurant.all()
    return render(request, 'pizzas/description.html',
                  {'product': pizza, 'products': pizzas, 'lower_price': pizza.price - 1000,
                   'upper_price': pizza.price + 1000, 'home': 'home_pizzas', 'pr': 'pizza', 'restaurants': restaurants})


def about_us(request):
    return render(request, 'pizzas/about_us_page.html')


def our_products(request):
    context = {
        'pizzas': Pizza.objects.all(),
        'burgers': Burger.objects.all()
    }
    return render(request, 'pizzas/all_products.html', context)


def search_pizzas(request):
    if request.method == "POST":
        searched_val = request.POST['searched_val']
        length_of_search = len(searched_val)
        filtered = Pizza.objects.filter(name__contains=searched_val)
        return render(request, 'pizzas/search_pizzas.html',
                      {'searched_val': searched_val, 'filtered': filtered, 'length_of_search': length_of_search})
    return render(request, 'pizzas/search_pizzas.html', {})


def main_page(request):
    return render(request, 'pizzas/main_website_page.html', {})


def home_burgers(request):
    context = Burger.objects.all()
    paginator = Paginator(context, 6)  # Show 6 pizzas per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pizzas/products_home.html', {'products': context, 'page_obj': page_obj, 'pr': 'burger'})


def burger_detail(request, id):
    burgers = Burger.objects.all()
    burger = get_object_or_404(Burger, id=id)
    restaurants = burger.restaurant.all()
    return render(request, 'pizzas/description.html',
                  {'product': burger, 'products': burgers, 'lower_price': burger.price - 1000,
                   'upper_price': burger.price + 1000, 'home': 'home_burgers', 'pr': 'burger',
                   'restaurants': restaurants})


def home_restaurants(request):
    context = Restaurants.objects.all()
    paginator = Paginator(context, 6)  # Show 6 pizzas per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pizzas/restaurants_main.html', {'Restaurants': context, 'page_obj': page_obj})


def restaurant_detail(request, id):
    restaurant = get_object_or_404(Restaurants, id=id)
    burgers = restaurant.burgers.all()
    pizzas = restaurant.pizzas.all()
    return render(request, 'pizzas/restaurant_description.html',
                  {'restaurant': restaurant, 'burgers': burgers, 'pizzas': pizzas})
