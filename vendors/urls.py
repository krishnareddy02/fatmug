from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('home_page',views.home_page,name="home_page"),
    path('purchase_order',views.purchase_order,name="purchase_order"),
    path('vender_data',views.vender_data,name="vender_data"),
    path('fulfillment_rate',views.fulfillment_rate,name="fulfillment_rate"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('purchase_order_details',views.purchase_order_details,name="purchase_order_details"),
    # path('vender',views.vender,name="vender"),
    path('vender_page',views.vender_page,name="vender_page"),
    path('delete1/<int:id>',views.delete1,name="delete1"),

]