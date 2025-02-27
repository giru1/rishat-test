from django.urls import path
from .views import buy_item, item_detail, item_list, home

urlpatterns = [
    path('buy/<int:id>/', buy_item, name='buy_item'),
    path('item/<int:id>/', item_detail, name='item_detail'),
    path('items/', item_list, name='item_list'),
    path('', home, name='home page'),
]