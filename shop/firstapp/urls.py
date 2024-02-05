from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="home"),
    path('about', views.about_page, name="about"),
    path('orders/', views.all_orders, name="all_orders"),
    path('items/', views.all_items, name="all_items"),
]
