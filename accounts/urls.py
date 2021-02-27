from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('accounts/sign_up/',views.sign_up,name="sign-up"),
    path('accounts/loged_out/', views.loged_out, name="logg-out"),
    path('accounts/', views.index, name="index")
]