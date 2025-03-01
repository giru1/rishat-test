from django.db import models

# Create your models here.
class Item(models.Model):
    CURRENCY_CHOICES = [
        ('usd', 'USD'),
        ('rub', 'RUB'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='usd')  # Добавлено поле для валюты

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    items = models.ManyToManyField(Item)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='usd')  # Валюта заказа

    def __str__(self):
        return f"Order {self.id} - Total: {self.total_price} {self.currency}"

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'


class Discount(models.Model):
    code = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Скидки'
        verbose_name_plural = 'Скидки'


class Tax(models.Model):
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=5, decimal_places=2)  # Процент налога

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Налоги'
        verbose_name_plural = 'Налоги'