from django import forms
from Users.models import Person
from events.models import Event
from datetime import date
class EventForm (forms.Form):
    CATEGORY_CHOICES = ( ('Music','Music'), ('sport','Sport'), ('Cinema','Cinema') )

    title= forms.CharField(
        label='Title',
        max_length=150,
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'id':"title",
                'placeholder':"Enter your title here"
        
        }
        )
    )
    description=forms.CharField(
        widget=forms.Textarea
    )
    imageEvent = forms.ImageField(
        label='Image'
    )
    nbParticipants = forms.IntegerField(
        label="Number",min_value=0,step_size=1
    )
    category = forms.ChoiceField(
        widget=forms.RadioSelect,choices=CATEGORY_CHOICES
    )
    dateEvent = forms.DateField(
        widget= forms.DateInput(
        attrs={
        'type':'date',
        'class':'form-contorl date-input'
        }
        )
    )
    organizer = forms.ModelChoiceField(
        queryset=Person.objects.all()
    )

class EventModelForm(forms.ModelForm):
    class Meta:
        model=Event
        field= "all"
        exclude= ['state']
        help_texts= {
            'title': 'Your event title here'
        }
        dateEvent = forms.DateField(
        initial = date.today,
        widget=forms.DateInput(
        attrs={
            'type':'date',
            'class':'form-control'
        
        }
        )

    )