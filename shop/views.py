import stripe
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Item
# Create your views here.

stripe.api_key = 'sk_test_51QwmYxP1QaLd00wovzYbHSFuy7g3L82dbx9Z0z2kq8WpzufhfZXXyBvz22yzEXOU1fsEpIgbyAwreOrNZy9GRGNn00j6nFKZ0c'

def buy_item(request, id):
    item = get_object_or_404(Item, id=id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',  # или другая валюта
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': int(item.price * 100),  # цена в центах
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/success/',
        cancel_url='http://localhost:8000/cancel/',
    )
    return JsonResponse({'id': session.id})

def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'item_detail.html', {'item': item})


def item_list(request):
    items = Item.objects.all()  # Получаем все товары
    return render(request, 'item_list.html', {'items': items})

def home(request):
    return render(request, 'home.html')