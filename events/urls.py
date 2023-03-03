from django.urls import path
from .views import *
from events.views import homePage,homePage1,listEventsStatic,listEvents,addEvent,add_Event
urlpatterns =[
    path('',homePage, name="home_page"),
    path('home/', homePage1 , name="home-page1"),
    path('listStatic/', listEventsStatic , name="Events_list"),
    path('listEvents/', listEvents , name="Events_list2"),
    path('listV/', EventListView.as_view(), name="Events_listV"),
    path('detail/<int:id>', detailEvent, name="Event_details"),
    # pk with the class primary key 
    path('detailV/<int:pk>', EventDetails.as_view(), name="Event_detailsV"),
    path('participate/<int:id>', Participate, name="participate_event"),
    path('addEvent/', addEvent, name="add_event"),
    path('deleteEventV/<int:id>', deleteEvent, name="delete_eventV"),
    path('updateEvent/<int:pk>', EventUpdateView.as_view(), name="update_event"),
    path('deleteEvent/<int:pk>', EventDeleteView.as_view(), name="delete_event"),
    path('addEventV/', add_Event, name="add_eventV"),
    path('addEventV2/', EventCreateView.as_view(), name="add_eventV2")



]