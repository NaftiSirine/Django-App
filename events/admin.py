from django.contrib import admin,messages
from .models import Event
from .models import Participation

# Register your models here.

# Register your models here.
# TabularInline et StackedInline POUR L AFFICHAGE
class ParticipationFilter(admin.SimpleListFilter):
    title = 'Participations'
    parameter_name ='nbParticipants'
    def lookups(self, request, model_admin):
        return ( 
            ('0' , ('No participants')),
            ('more', ('there are participants')),
        )
    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(nbParticipants__exact=0)
        if self.value() == 'more' :
            return queryset.filter(nbParticipants__gt=0)
# exact et gt  : lookups = where nbr par 0 
# participation inline
class ParticipationInline(admin.TabularInline):
    model = Participation
    extra = 1
    classes =['collapse']
    can_delete=False
    readonly_fields=('datePart',)
def set_state(ModelAdmin,request,queryset):
    rows=queryset.update(state=True)
    if (rows == 1):
        msg= "One event was "
    else:
        msg= f"{rows} events were"
    messages.success(request , message='%s successfully accepted'%msg)

set_state.short_description="ACCEPT EVENT"

class EventAdmin(admin.ModelAdmin):
    def unset_state(self,request,queryset):
        rows_filter = queryset.filter(state=False)
        if rows_filter.count()>0 :
             messages.error(request , message=f"{rows_filter.count()} is already REFUSED")
        else:
            rows = queryset.update(state=False)
            if(rows == 1):
                msg=  "One event was "
            else :
                msg =  f"{rows} events were"
            messages.success(request , message='%s successfully refused' % msg)

    unset_state.short_description="rEFUSE EVENT"

    actions= [set_state,unset_state]
    actions_on_bottom= True 
    actions_on_top =False
    inlines = [ParticipationInline]
    list_per_page= 20 
    list_display=(
        'title',
        'category',
        'state',
    )
    # filtre
    list_filter = (
        'state',
        'category',
        ParticipationFilter,
    )
    #trie by ordre alphabitique selon le titre 
    ordering = ('title',)
    search_fields =[
        'title',
        'category'
    ]
    readonly_fields =('createdAt',)
    autocomplete_fields=['organizer']
    #  'classes': ('collapse',),  to hide about section
    fieldsets = (
        (
            'State',
            {
                'fields': ('state',)
            }
        ),
        (
            'About',
            {
                'classes': ('collapse',),
                'fields': (
                    'title',
                    'imageEvent',
                    'category',
                    'organizer',
                    'nbParticipants',
                    'description',
                ),
            }
        ),
        (
            'Dates',
            {
                'fields': (
                    (
                        'dateEvent',
                        'createdAt'
                    ),
                )
            }
        ),
    )
admin.site.register(Event,EventAdmin)
