from django.urls import path

from product.urls import urlpatterns
from . import views

urlpatterns=[
    path('', views.mainpage),
    path('company/', views.company),
]