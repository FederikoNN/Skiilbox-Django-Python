from django.contrib import admin
from .models import Shop, Item, ItemInShop, Cart,Purchase

admin.site.register(Shop)
admin.site.register(Item)
admin.site.register(ItemInShop)
# admin.site.register(Cart)
admin.site.register(Cart)
admin.site.register(Purchase)
