from django.urls import path
from .views import *
from events.views import homePage,homePage1,listEventsStatic,listEvents
urlpatterns =[
    path('',homePage, name="home_page"),
    path('home/', homePage1 , name="home-page1"),
    path('listStatic/', listEventsStatic , name="Events_list"),
    path('listEvents/', listEvents , name="Events_list2"),
]