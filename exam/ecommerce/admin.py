from django.contrib import admin

# Register your models here.
from ecommerce.models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
