from django.urls import path
from .views import ItemListView, ShopSingleView, ItemSingleView, CartView

urlpatterns = [
    path('', ItemListView.as_view(), name='main'),
    path('<int:pk_shop>/shop_single/', ShopSingleView.as_view(),
         name='shop_single'),
    path('<int:pk_shop>/shop_single/<int:pk>/item_single/',
         ItemSingleView.as_view(), name='item_single'),
    path('cart/', CartView.as_view(), name='cart'),
]
