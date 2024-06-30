from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('condition/', views.condition_add, name='condition'),
    path('cities/', views.search_city, name='search'),
]
