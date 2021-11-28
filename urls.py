from django.urls import path
from . import views # the period means "from this directory (that we are inside)" import this file

urlpatterns = [ # why is it using these brakets?
    # Path Converters
    # int: integers
    # str: strings
    # path: whole urls / 
    # slugs : hpyhen-and_underscores_stuff
    # UUID: universally unique identifier
    path('', views.home, name="home"), # pointing to the views file, home function
    path('<int:year>/<str:month>/', views.home, name="home"), 
    # since we added year and month here, we must go to views.py 
    # to add them into the parameters of home because those variables
    # are redirected to the function "home" in the "views" py file,
    # where they will be processed.
    path('comedance', views.comedance, name="comedance"), 
    path('aboutpage', views.aboutpage, name="aboutpage"), 
    path('contact', views.contact, name="contact"), 
    path('gallery', views.gallery, name="gallery"), 
    path('musicdvds', views.musicdvds, name="musicdvds"), 
]
