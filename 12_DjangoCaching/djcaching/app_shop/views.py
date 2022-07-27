from django.views.generic import ListView
from .models import Shop


class ShopListView(ListView):
    model = Shop
    template_name = 'shop/shop_list.html'
    context_object_name = 'shop_list'
