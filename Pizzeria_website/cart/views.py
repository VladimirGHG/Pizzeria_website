from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from pizzas.models import Pizza, Burger

from .cart import Cart


def view_cart(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    return render(request, "cart/view_cart.html", {"cart_products": cart_products})


def add_cart(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get('product_id'))
        # product_type = request.POST.get('product_type')
        product = get_object_or_404(Pizza, id=product_id)
        # print(product_type)
        # if product_type == 'pizza':
        #     product = get_object_or_404(Pizza, id=product_id)
        # elif product_type == 'burger':
        #     product = get_object_or_404(Burger, id=product_id)
        # else:
        #     return JsonResponse({'error': 'Invalid product type'}, status=400)

        cart.add(product=product)
        response = JsonResponse({'Product Name': product.name})
        return response
