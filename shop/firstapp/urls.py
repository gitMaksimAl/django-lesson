from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="home"),
    path('about', views.about_page, name="about"),
    path('orders/', views.all_orders, name="all_orders"),
    path('items/', views.all_items, name="all_items"),
    path('item/<int:item_pk>', views.get_item, name="item"),
    path("orders/<int:client_pk>", views.client_orders, name="order"),
    path('items/new', views.add_item, name="add_item"),
    path('images/new', views.add_image, name="add_image"),
]
