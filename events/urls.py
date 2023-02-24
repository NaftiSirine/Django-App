from django.urls import path
from .views import *
from events.views import homePage,homePage1,listEventsStatic,listEvents
urlpatterns =[
    path('',homePage, name="home_page"),
    path('home/', homePage1 , name="home-page1"),
    path('listStatic/', listEventsStatic , name="Events_list"),
    path('listEvents/', listEvents , name="Events_list2"),
    path('listV/', EventListView.as_view(), name="Events_listV"),
    path('detail/<int:id>', detailEvent, name="Event_details"),
    # pk with the class primary key 
    path('detailV/<int:pk>', EventDetails.as_view(), name="Event_detailsV"),



]