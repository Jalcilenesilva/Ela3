
from .views import home,second
from django.urls import path


urlpatterns = [
    path('',home,name="home"),
    path('second/', second,name="home"),

]