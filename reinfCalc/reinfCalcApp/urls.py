from django.urls import path, include
from reinfCalcApp import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]