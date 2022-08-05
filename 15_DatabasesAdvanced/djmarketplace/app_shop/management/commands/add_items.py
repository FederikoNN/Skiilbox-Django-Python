import random
from ...models import Item, ItemInShop, Shop
from django.core.management import BaseCommand


class Command(BaseCommand):
    def add_items(self):
        shops = Shop.objects.all()
        for item_id in range(1000):
            item = Item.objects.create(name=f'Item #{item_id}',
                                       price=random.randint(0, 10000))
            shop = random.choice(shops)
            quantity = random.randint(1, 500)
            ItemInShop.objects.create(items=item, shop=shop, quantity=quantity)

    # def delete_items(self):
    #     items_exclude = ['Колокольчик', 'Смартфон', 'Картофель', 'Монитор',
    #                      'Клавиатура']
    #     items = Item.objects.all()
    #     for item in items:
    #         if item.name not in items_exclude:
    #             item.delete()

    def handle(self, *args, **options):
        self.add_items()
