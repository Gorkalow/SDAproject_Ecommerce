from django.shortcuts import render
from .models import *

# Create your views here.

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        #get_or_create function first tries to query an object with certain values
        # if that object doesn't exist, it creates it. We want an order with opened cart, thus setting complete to False
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        #we're able to query child objects like 'orderitem_set' by setting a value of parent objects like 'order'
        items = order.orderitem_set.all()
    else:
        items = []

    context = {'items':items}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
