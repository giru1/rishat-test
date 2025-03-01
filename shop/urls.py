from django.urls import path
from .views import buy_item, item_detail, item_list, home, create_order, create_payment_intent

urlpatterns = [
    path('', home, name='home page'),
    path('buy/<int:id>/', buy_item, name='buy_item'),

    path('item/<int:id>/', item_detail, name='item_detail'),
    path('items/', item_list, name='item_list'),

    path('create-order/', create_order, name='create_order'),

    path('create-payment-intent/<int:order_id>/', create_payment_intent, name='create_payment_intent'),
]