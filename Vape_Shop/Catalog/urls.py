from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.catalog, name='main_catalog'),
    path('make_offer/', views.make_offer, name='make_offer'),
]
