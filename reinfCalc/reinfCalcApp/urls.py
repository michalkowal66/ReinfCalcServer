from django.urls import path
from reinfCalcApp import views


app_name = 'reinfCalcApp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('profile/', views.ProfileInfoView.as_view(), name='profile-info'),
    path('results/', views.ResultsListView.as_view(), name='results'),
    path('results/<int:task_id>', views.ResultsReportView.as_view(), name='results-report'),
    path('run-calculations/', views.run_calculation, name='run-calculation'),
    path('auth-app-user/', views.auth_app_user, name='auth-app-user'),
]