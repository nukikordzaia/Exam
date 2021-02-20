from datetime import datetime
from decimal import Decimal
from typing import Dict, Optional
from typing import NewType

from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, Q
from django.shortcuts import render
from django.utils import timezone

from ecommerce.forms import OrderForm
from ecommerce.models import Order
from user.forms import User

OptDecimal = NewType('Optional Decimal', Optional[Decimal])


@login_required
def order_detail(request):
    order_form = OrderForm()
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order: Order = order_form.save(commit=False)
            try:
                start_date = datetime.strptime(
                    " ".join([
                        order_form.cleaned_data['start_date_day'],
                        order_form.cleaned_data['start_date_time']
                    ]),
                    '%d/%m/%Y %H:%M'
                )
                order.start_date = start_date
                order.save()
            except ValueError:
                order_form.add_error('start_date_day', 'please, enter correct data ')

    now = timezone.now()
    user_order_info: Dict[str, OptDecimal] = request.user.orders.filter(end_date__isnull=False). \
        aggregate(
        spent_money_year=Sum(
            'price',
            filter=Q(end_date__gte=now - timezone.timedelta(days=365))
        ),
        bought_last_year=Count(
            'id',
            filter=Q(end_date__gte=now - timezone.timedelta(days=365))
        ),
        spent_money_month=Sum(
            'price',
            filter=Q(end_date__gte=now - timezone.timedelta(weeks=4))
        ),
        bought_last_month=Count(
            'id',
            filter=Q(end_date__gte=now - timezone.timedelta(weeks=4))
        ),
        spent_money_week=Sum(
            'price',
            filter=Q(end_date__gte=now - timezone.timedelta(days=7))
        ),
        bought_last_week=Count(
            'id',
            filter=Q(end_date__gte=now - timezone.timedelta(days=7))
        )
    )
    return render(request, template_name='ecommerce/order-detail.html', context={
        'user': User,
        'user_order_info': user_order_info,
        'order_form': order_form
    })
