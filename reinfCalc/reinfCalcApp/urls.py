from django.urls import path
from reinfCalcApp import views


app_name = 'reinfCalcApp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('profile/', views.ProfileInfoView.as_view(), name='profile-info'),
    path('results/', views.ResultsView.as_view(), name='results'),
    path('upload-file/', views.upload_file, name='upload-file'),
    path('auth-app-user/', views.auth_app_user, name='auth-app-user'),
]