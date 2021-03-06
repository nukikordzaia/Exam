from django.urls import path

from user.views import user_registration, user_login, user_logout

app_name = 'user'

urlpatterns = [
    path('registration/', user_registration, name='user_registration'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),

]
