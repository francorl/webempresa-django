from django.urls import path 
from . import views
from services import views as services_views


urlpatterns = [

    path('about/',views.about, name="about"),
    path('services/',services_views.service, name="services"),
    path('store/', views.store, name="store"),
    path('contact/',views.contact, name="contact"),
    path('', views.home, name="home"),
]




