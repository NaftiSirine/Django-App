from django.contrib import admin
from .models import Person
# Register your models here.

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display=(
        'email',
        'cin',
    )
    # filtre
    list_filter = (
        'email',
    )
    #trie by ordre alphabitique selon le titre 
    ordering = ('email',)
    search_fields =[
        'email',
        'cin'
    ]
    readonly_fields =('createdAt',)
    #  'classes': ('collapse',),  to hide about section
    fieldsets = (
        (
            'Email and Username',
            {
                'fields': ('email','username',)
            }
        ),
        (
            'Cin',
            {
                'classes': ('collapse',),
                'fields': (
                    'password',
                    'cin',
                ),
            }
        ),
        (
            'Dates',
            {
                'fields': (
                    (
                    
                        'createdAt'
                    ),
                )
            }
        ),
    )
admin.site.register(Person,PersonAdmin)