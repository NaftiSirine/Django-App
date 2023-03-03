from django.urls import path
from .views import *
from Users.views import *
urlpatterns =[
    path('',login_view, name="login_view"),
   



]