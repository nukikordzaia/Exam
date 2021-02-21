from django.urls import path
from . import views

app_name = 'ecommerce'

urlpatterns = [
    path("", views.home, name="home"),
    path('home/', views.home, name="home"),
    path("orders/", views.order_detail, name="orders"),
    path("tickets/", views.user_tickets, name="user_tickets"),

]