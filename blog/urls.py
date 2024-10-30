from django.urls import path
from .views import *

urlpatterns = [
    path('', blog_view, name='blog'),
    path('category/<str:cat_name>', blog_view, name='category'),

]