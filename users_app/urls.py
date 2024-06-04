from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.listBook, name='userlist'),
    path('user-details/<int:book_id>/', views.detailView, name='userdetails'),
    path('search-user/', views.searchBook, name='usersearch'),
    path('user_add_to_cart/<int:book_id>/', views.add_to_cart, name='addtocart'),
    path('view-cart/', views.view_cart, name='viewcart'),
    path('increase/<int:item_id>/', views.increase_quantity, name='increaseq'),
    path('decrease/<int:item_id>/', views.decrease_quantity, name='decreaseq'),
    path('remove-cart/<int:item_id>/', views.remove_from_cart, name='removecart'),
    path('checkout-session/', views.createCheckout, name='checkout_session'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),

]