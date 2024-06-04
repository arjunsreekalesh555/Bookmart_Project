from django.urls import path
from . import views
urlpatterns=[

    path('userregister/', views.Registration, name='register'),
    path('userlogIn/', views.logIn, name='login'),
    path('userlogOut/', views.logOut, name='logout'),

]