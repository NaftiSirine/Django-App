from django.contrib import admin
from .models import Event
# Register your models here.

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display=(
        'title',
        'category',
        'state',
    )
    # filtre
    list_filter = (
        'state',
        'category'
    )
    #trie by ordre alphabitique selon le titre 
    ordering = ('title',)
    search_fields =[
        'titre',
        'category'
    ]
    readonly_fields =('createdAt',)
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
