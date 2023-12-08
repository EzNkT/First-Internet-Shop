from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('rules/', views.rules, name='rules'),
    path('help/', views.help, name='help'),
    path('adress/', views.adress, name='adress'),
]