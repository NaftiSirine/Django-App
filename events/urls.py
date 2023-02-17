from django.urls import path
from .views import *
from Users.views import homePage,homePage1,listEventsStatic
urlpatterns =[
    path('',homePage, name="home_page"),
    path('home/', homePage1 , name="home-page1"),
    path('listStatic/', listEventsStatic , name="Events_list"),
]