
from django.urls import path
from . import views


app_name = 'face_to_site'

urlpatterns = [

    path('home', views.home, name='home'),
    path('open_to_fairi_tales', views.open_to_fairi_tales, name='open_to_fairi_tales'),

]
