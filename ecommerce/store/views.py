from django.shortcuts import render
from django.http import JsonResponse
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
        #creating values for unauthenticated user to prevent error while accessing empty cart
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items':items, 'order':order}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    return JsonResponse('Item was added', safe=False)