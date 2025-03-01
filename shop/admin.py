from django.contrib import admin

from shop.models import Item, Order, Discount, Tax


# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'currency')
    list_filter = ('currency',)


admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Discount)
admin.site.register(Tax)