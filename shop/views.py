import stripe
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Order, Discount, Tax
from django.middleware.csrf import get_token

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

def create_order(request):
    if request.method == 'POST':
        item_ids = request.POST.getlist('item_ids')  # Получаем ID товаров из POST-запроса

        # Проверка на наличие идентификаторов
        if not item_ids:
            return redirect('item_list')  # Если нет выбранных товаров, перенаправляем обратно

        items = Item.objects.filter(id__in=item_ids)

        total_price = sum(item.price for item in items)
        currency = items.first().currency if items else 'usd'  # Определяем валюту

        # Получаем все доступные скидки и налоги
        discounts = Discount.objects.all()
        taxes = Tax.objects.all()

        order = Order.objects.create(total_price=total_price, currency=currency)
        order.items.set(items)  # Устанавливаем связанные товары

        # Передаем данные на страницу заказа
        return render(request, 'order.html', {
            'items': items,
            'total_price': total_price,
            'currency': currency,
            'discounts': discounts,
            'taxes': taxes,
            'order_id': order.id,
            'csrf_token': get_token(request),
        })
    else:
        return redirect('item_list')

def create_payment_intent(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    items = order.items.all()

    # Создание Payment Intent
    line_items = []
    for item in items:
        line_items.append({
            'price_data': {
                'currency': order.currency,
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': int(item.price * 100),  # цена в центах
            },
            'quantity': 1,
        })

    payment_intent = stripe.PaymentIntent.create(
        amount=int(order.total_price * 100),  # общая стоимость в центах
        currency=order.currency,
        payment_method_types=['card'],
    )

    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id)

        return JsonResponse({'client_secret': payment_intent['client_secret']})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)