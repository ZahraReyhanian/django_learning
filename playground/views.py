from django.forms import DecimalField
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.db.models.aggregates import  Min, Avg
from django.db.models import Q, F, Value, Func, ExpressionWrapper, Count, Max, Sum
from django.db.models.functions import Concat
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from store.models import OrderItem, Product, Order, Customer, Collection
from tags.models import TaggedItem
# Create your views here.


def say_hello(request):
    # queryset = OrderItem.objects.filter(product__collection__id=3)
    # queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # queryset = Product.objects.filter(inventory=F('unit_price'))
    # queryset = Product.objects.order_by('inventory', '-title').reverse()[0]
    # queryset = Product.objects.latest('unit_price')
    # queryset = Product.objects.values('id', 'title', 'Collection__title')
    # queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    # queryset = Product.objects.select_related('Collection').all()
    # queryset = Product.objects.prefetch_related('promotions').all()
    # queryset = Product.objects.prefetch_related('promotions').select_related('Collection').all()
    # queryset = Order.objects.select_related(
    #     'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # result = Product.objects.filter(Collection__id=6).aggregate(
    #     count=Count('id'), min_price=Min('unit_price'))
    # queryset = Customer.objects.annotate(is_new=Value(True))
    # queryset = Customer.objects.annotate(new_id=F('id') + 1) # create new_id column that is id + 1
    # queryset = Customer.objects.annotate(
    #     full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
    # )
    # queryset = Customer.objects.annotate(
    #     full_name=Concat('first_name', Value(' '), 'last_name')
    # )
    # queryset = Customer.objects.annotate(
    #     orders_count=Count('order')  # number of orders for each customer
    # )
    # discounted_price = ExpressionWrapper(
    #     F('unit_price') * 0.8, output_field=DecimalField())

    # queryset = Product.objects.annotate(discounted_price=discounted_price)

    # queryset = Customer.objects.annotate(last_order_id=Max('order__id'))

    # queryset = Collection.objects.annotate(product_count=Count('product'))

    # queryset = Customer.objects.annotate(count_order=Count('order__id')).filter(count_order__gt=5)

    # queryset = Customer.objects.annotate(total_spent=Sum(
    #     F('order__orderitem__unit_price') *
    #     F('order__orderitem__quantity')
    # ))

    # queryset = Product.objects.annotate(total_sale=Sum(
    #     F('orderitem__unit_price') *
    #     F('orderitem__quantity')
    # )).order_by('-total_sale')[:5]

    queryset = TaggedItem.objects.get_tags_for(Product, 1)

    return render(request, 'hello.html', {'name': 'Zahra', 'tags': list(queryset)})