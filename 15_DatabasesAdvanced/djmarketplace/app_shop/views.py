import datetime

from django.shortcuts import redirect, reverse
from django.views.generic import ListView, DetailView
from .models import Item, Shop, ItemInShop, Cart, Purchase
from .forms import CartViewForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, F
import logging

logger = logging.getLogger(__name__)

BONUS = 10  # Bonus in percent


class ItemListView(ListView):
    model = Item
    template_name = 'shop/item_list.html'
    context_object_name = 'item_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shops = []
        report = Purchase.objects.values('product').annotate(
            item_quantity=Sum('quantity')).order_by('-item_quantity').first()
        if report:
            product = Item.objects.get(id=report['product'])
            report['product'] = product.name
            report['id'] = product.id
        for item_id in Item.objects.prefetch_related('shops').all():
            shops_item = [shop.name for shop in item_id.shops.all()]
            if shops_item:
                shops.append(
                    {'id': item_id.id, 'name': item_id.name,
                     'shops': shops_item})
        context['shops'] = shops
        context['shop_list'] = Shop.objects.all()
        context['bestseller'] = report
        return context


class CartView(LoginRequiredMixin, ListView):
    model = Cart
    template_name = 'shop/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.filter(user_id=self.request.user.id)
        context['cart_list'] = cart
        context['cart_cost'] = cart.aggregate(
            total=Sum(F('product__price') * F('quantity')))['total']
        if cart:
            logger.info(
                f'{datetime.datetime.now()} User {self.request.user} placed an '
                f'order')
        return context

    def post(self, request, *args, **kwargs):
        cart = Cart.objects.filter(user_id=request.user.id)
        user = request.user
        status = user.account.status
        status_previous = user.account.status_previous
        if status != status_previous:
            user.account.status_previous = status
            user.account.save(update_fields=['status_previous'])
        if 'pay' in request.POST:
            total_cost = 0
            for item in cart:
                total_cost += item.total_cost
                item_in_shop = ItemInShop.objects.get(shop=item.shop,
                                                      items=item.product)
                Purchase.objects.create(
                    user=user,
                    product=item.product,
                    quantity=item.quantity,
                    cost=item.total_cost
                )
                item_in_shop.quantity = F('quantity') - item.quantity
                user.account.balance = F('balance') - item.total_cost
                user.account.status_points = F(
                    'status_points') + item.total_cost * BONUS / 100
                user.account.save()
                item_in_shop.save()
                item.delete()
            logger.info(
                f'{datetime.datetime.now()}  Debiting {total_cost} from the '
                f'balance of user '
                f'{user.username}')
        elif 'refuse' in request.POST:
            for item in cart:
                item.delete()
        return redirect(reverse('main'))


class ShopSingleView(ListView):
    model = ItemInShop
    template_name = 'shop/shop_single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shop_items'] = ItemInShop.objects.select_related('shop',
                                                                  'items').filter(
            shop_id=self.kwargs['pk_shop']).all()
        return context


class ItemSingleView(DetailView):
    model = Item
    template_name = 'shop/item_single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk_shop']
        pk_item = self.kwargs['pk']
        item = ItemInShop.objects.filter(
            items_id=pk_item).get(shop_id=pk)
        context['items_shop'] = item
        context['cart_form'] = CartViewForm
        return context

    def post(self, request, *args, **kwargs):
        cart_object = self.get_object()
        shop = Shop.objects.get(pk=self.kwargs['pk_shop'])
        cart_form = CartViewForm(request.POST)
        if cart_form.is_valid():
            cart = cart_form.save(commit=False)
            cart.user = self.request.user
            cart.product = cart_object
            cart.shop = shop
            cart.save()
        return redirect(
            reverse('shop_single', kwargs={'pk_shop': self.kwargs['pk_shop']}))
