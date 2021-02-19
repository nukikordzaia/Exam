from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
from ecommerce.forms import OrderForm
from ecommerce.models import Order


def orders(request):
    order_list = Order.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(order_list, 5)
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    order_form = OrderForm()
    if request.method == 'POST':
        print(request.POST)
        order_form=OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
    context = {
        'orders': orders,
        'order_form': order_form,
    }
    return render(request=request, template_name='ecommerce/order.html', context=context)
