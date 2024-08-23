from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PizzaForm, BurgerForm, RestaurantForm
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
    products = Burger.objects.all()
    paginator = Paginator(products, 6)  # Show 6 pizzas per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pizzas/products_home.html', {'products': products, 'page_obj': page_obj, 'pr': 'burger'})


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
    return render(request, 'restaurants/restaurants_main.html', {'Restaurants': context, 'page_obj': page_obj})


def restaurant_detail(request, id):
    restaurant = get_object_or_404(Restaurants, id=id)
    burgers = restaurant.burgers.all()
    pizzas = restaurant.pizzas.all()
    return render(request, 'restaurants/restaurant_description.html',
                  {'restaurant': restaurant, 'burgers': burgers, 'pizzas': pizzas})


def create_product(request):
    pizza_form = PizzaForm()
    burger_form = BurgerForm()

    if request.method == "POST":
        if 'pizza_submit' in request.POST:
            pizza_form = PizzaForm(request.POST, request.FILES)
            if pizza_form.is_valid():
                pizza_form.save()
                return redirect("main_page")
        elif 'burger_submit' in request.POST:
            burger_form = BurgerForm(request.POST, request.FILES)
            if burger_form.is_valid():
                burger_form.save()
                return redirect("main_page")

    return render(request, 'pizzas/create_product_main.html', {'pizza_form': pizza_form, 'burger_form': burger_form})


def update_burger(request, burger_id):
    burger = get_object_or_404(Burger, id=burger_id)

    if request.method == 'POST':
        form = BurgerForm(request.POST, instance=burger)
        if form.is_valid():
            form.save()
            return redirect('burger_detail', id=burger_id)
    else:
        form = BurgerForm(instance=burger)

    return render(request, 'pizzas/update_burger.html', {'form': form, 'burger': burger})


def update_pizza(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)

    if request.method == 'POST':
        form = PizzaForm(request.POST, instance=pizza)
        if form.is_valid():
            form.save()
            return redirect('pizza_detail', id=pizza_id)
    else:
        form = PizzaForm(instance=pizza)

    return render(request, 'pizzas/update_pizza.html', {'form': form, 'pizza': pizza})

def add_restaurant(request):
    restaurant_form = RestaurantForm()
    if request.method == "POST":
        restaurant_form = RestaurantForm(request.POST, request.FILES)
        if restaurant_form.is_valid():
            restaurant_form.save()
            return redirect("main_page")
    return render(request, 'restaurants/create_restaurant.html', {'restaurant_form': restaurant_form})
