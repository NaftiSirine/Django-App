from django.contrib import admin,messages
from .models import Person
# Register your models here.

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    def set_is_active(ModelAdmin,request,queryset):
        rows=queryset.update(is_active=True)
        if (rows == 1):
             msg= "One Person was "
        else:
             msg= f"{rows} persons were"
        messages.success(request , message='%s successfully activated'%msg)

    set_is_active.short_description="activate Person"


    actions= [set_is_active]
    list_display=(
        'email',
        'cin',
        'is_active'
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