from .views import *
from django.urls import path

urlpatterns = [
    path('', home , name='home'),
    path('login', login_page , name='login_page'),
    path('register', register_page , name='register_page'),
]
