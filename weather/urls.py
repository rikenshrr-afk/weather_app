
from django.urls import path,include
from weather import views

urlpatterns = [

    path('',views.home,name='home')
]