from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib import messages 
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
            'id': 1,
            'title': 'Event 1',
            'description':'description 1 ',
        },
        {
            'id': 15,
            'title':'Event 2',
            'description': 'description 2',
        },
        {
            'id': 12,
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
    queryset= Event.objects.filter(state=True)
    def get_queryset(self):
        return Event.objects.filter(state=True)

class EventDetails(DetailView):
    model = Event

def addEvent(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)

        if form.is_valid():
            Event.objects.create(
                **form.cleaned_data
                
            )
            return redirect('Events_listV')
        
    return render(
        request,
        'events/event_add.html',
        {
            'form': form,
        }
    )     
  
def add_Event(request):
    form = EventModelForm()
    if request.method == 'POST':
        form = EventModelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('Events_listV')
        
    return render(
        request,
        'events/event_add.html',
        {
            'form': form,
        }
    )      
def deleteEvent(request,id):
    event = Event.objects.get(id=id)
    if event.delete():
        return redirect('Events_listV')


    return render(
        request,
        'events/event_confirm_delete.html',
        {
            'event': event,
        }
    )      

class EventCreateView(CreateView):
    model = Event
    form_class= EventModelForm
    template_name='events/event_add.html'
    success_url= reverse_lazy('Events_listV')
class EventUpdateView(UpdateView):
    model = Event
    form_class = EventModelForm
    success_url = reverse_lazy('Events_listV')
    template_name = 'events/event_add.html'
class EventDeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy('Events_listV')
    template_name = 'events/event_confirm_delete.html'
def Participate(request, id):
    event = Event.objects.get(id=id)
    person=Person.objects.get(email='sirine.nafti@esprit.tn')
    if Participation.objects.filter(person=person,event=event).count() == 0 :

        Participation.objects.create(person=person,event=event)
        event.nbParticipants+=1
        event.save()
        messages.add_message(request,messages.SUCCESS,f'Your participation to this event : {event.title} was added')
    else:
        messages.add_message(request,messages.ERROR,f'You r already participating to this event : {event.title} ')

    # method 2: 
    #nb = event.event.nbParticipants + 1
    #Event.objects.filter(id=id).update(nbParticipants=nb)
    return redirect('Events_listV')