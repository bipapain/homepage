
from django.urls import path
from . import views


app_name = 'cheatsheets'

urlpatterns = [
    path('', views.all_cheatsheets, name='all_cheatsheets'),
    path('<int:cheatsheet_id>/', views.detail, name='detail'),
]
