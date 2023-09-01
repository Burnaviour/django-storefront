from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.db.models import Q, F, Value, Count
from django.db import transaction
from django.db.models.functions import Concat
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer, Collection, Order, OrderItem
from tags.models import TaggedItem


def say_hello(request):

    # queryset = Product.objects.filter(id__in=OrderItem.objects.values(
    #     'product_id').distinct()).order_by('title')
    # queryset = Order.objects.select_related(
    #     'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # queryset = Product.objects.filter(collection__id=3).aggregate(
    #     Min_Price=Min('unit_price'), max_price=Max('unit_price'), Avg_Price=Avg('unit_price'))
    # print(queryset)
    # queryset = Customer.objects.annotate(is_new=F('id'))

    # queryset = Customer.objects.annotate(
    #     full_name=Concat('first_name', Value(' '), 'last_name'))
    # queryset = Customer.objects.annotate(
    #     Orders=Count('order'))

    # queryset = TaggedItem.objects.get_tags_for(Product, 1)
    # collection = Collection.objects.filter(pk=11).update(title='Games'
    #                                                      )
    # collection.save()
    # print(collection.id)
    with transaction.atomic():
        order = Order()
        order.customer_id = 1
        order.save()
        order_item = OrderItem()
        order_item.order = order
        order_item.product_id = 1
        order_item.quantity = 1
        order_item.unit_price = 200
        order_item.save()

    return render(request, 'hello.html', {'name': 'Muzafar'})
