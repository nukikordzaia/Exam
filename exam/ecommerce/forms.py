from django.core.validators import RegexValidator
from django.forms import ModelForm
from django.forms import ModelChoiceField, TextInput, DecimalField, CharField

from ecommerce.models import Ticket

from ecommerce.models import Order


class OrderForm(ModelForm):
    ticket = ModelChoiceField(queryset=Ticket.objects.all())
    price = DecimalField()
    start_date_day = CharField(widget=TextInput(attrs={
        'class': 'datepicker'
    }), validators=[RegexValidator(
        r'^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](21|20)\d\d$',
        message='this is correct format: dd/mm/yyyy'
    )])
    start_date_time = CharField(widget=TextInput(attrs={
        'class': 'timepicker'
    }), validators=[RegexValidator(r'^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$', message='this is correct format: MM:HH')])

    class Meta:
        fields = ('ticket',  'price', 'start_date_day', 'start_date_time',)
        model = Order