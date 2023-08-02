from django.urls import path
from shop.views import index,detail

urlpatterns = [
    path('', index, name='Home'),
    path('<int:myid>', detail, name='Detail')
]