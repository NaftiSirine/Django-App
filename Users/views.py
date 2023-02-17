from django.shortcuts import render
from django.http import HttpResponse

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