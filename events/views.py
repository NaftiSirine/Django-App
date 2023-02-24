from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
# Create your views here.
def homePage(request):
    return HttpResponse('<h1>Title Here</h1>')

def homePage1(request):
    return render(
        request,
        'events/homePage.html'
    )
def listEventsStatic(request):
    list= [
        {
            'title': 'Event 1',
            'description':'description 1 ',
        },
        {
            'title':'Event 2',
            'description': 'description 2',
        },
        {
            'title':'Event 3',
            'description':'description 3',
        }
    ]
    return render(
        request,
        'events/listEvents.html',
        {
            'events': list
        }
    )
def listEvents(request):
    list = Event.objects.all()
    return render(request, 
        'events/listEvents.html',
        {
        'events': list
        })
def detailEvent(request,id):
    event= Event.objects.get(id=id)
    return render(request,
        'events/event_detail.html',{
        'event' :event
                  })
class EventListView(ListView):
    model = Event
    template_name = 'events/listEvents.html'
    context_object_name = 'events'

class EventDetails(DetailView):
    model = Event