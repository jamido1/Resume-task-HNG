from django.urls import path
from page import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact', views.contact, name='contact')
]
