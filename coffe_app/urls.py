from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('about/', about_view, name='about'),
    path('service/', service_view, name='service'),
    path('menu/', menu_view, name='menu'),
    path('contact/', contact_view, name='contact'),

    ]