from django.db import models
from django.utils.translation import ugettext_lazy as _


class Ticket(models.Model):
    name = models.CharField(max_length=10, verbose_name=_('ticket name'))
    start_date = models.DateTimeField(verbose_name=_('start time'))
    end_date = models.DateTimeField(verbose_name=_('start time'))
    code = models.CharField(max_length=10, verbose_name=_('code'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Ticket')


class Order(models.Model):
    ticket = models.ForeignKey(
        to='Ticket',
        related_name='order',
        on_delete=models.PROTECT,
    )
    price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name=_('price'))
    start_date = models.DateTimeField(verbose_name=_('start order'))
    end_date = models.DateTimeField(verbose_name=_('start order'))
    user = models.ForeignKey(to='user.User', related_name='orders', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.ticket)

    class Meta:
        verbose_name = _('Order')


