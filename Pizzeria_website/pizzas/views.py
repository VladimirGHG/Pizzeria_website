from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Pizza


def home_pizzas(requests):
    context = Pizza.objects.all()
    paginator = Paginator(context, 6)  # Show 6 pizzas per page.

    page_number = requests.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(requests, 'pizzas/pizzas_home.html', {'pizzas': context, 'page_obj': page_obj})


def pizza_detail(request, id):
    pizzas = Pizza.objects.all()
    pizza = get_object_or_404(Pizza, id=id)
    return render(request, 'pizzas/description.html',
                  {'pizza': pizza, 'pizzas': pizzas, 'lower_price': pizza.price - 1000,
                   'upper_price': pizza.price + 1000})


def about_us(request):
    return render(request, 'pizzas/about_us_page.html')


def our_products(request):
    context = {
        'pizzas': Pizza.objects.all()
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
