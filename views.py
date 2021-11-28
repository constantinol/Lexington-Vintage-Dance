from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):  
    # added year and month in the parameters
    # the {} in render is the context dictionary, which allows us to pass things from the backend to the frontend
    name = "Micho"
    month=month.capitalize() # just in case it is not already capitalized
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number) # to make sure it is an integer, not a string

    # make a calendar
    cal = HTMLCalendar().formatmonth(
        year, 
        month_number)
    
    # **experimental** to get current date
    now = datetime.now()    # now() is a function in 
    current_year=now.year
    
    # what we can pull into the HTML file 
    # always add anything you want to add here!
    return render(request, 
        'home/home.html', {
        "name" : name,   # this is just a way to pull from back-end to front with python
        "year" : year,
        "month" : month,    # getting these from what is being passed in
        "month_number" : month_number,
        "cal": cal,
        "current_year": current_year,
    })   #points to the home html page

def comedance (request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    month=month.capitalize() # just in case it is not already capitalized
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number) # to make sure it is an integer, not a string

    # make a calendar
    cal = HTMLCalendar().formatmonth(
        year, 
        month_number)
    
    # Getting current time for copyright section
    now=datetime.now()
    current_year=now.year
    
    return render(request,
    'home/comedance.html', {
        "year" : year,
        "month" : month,    # getting these from what is being passed in
        "month_number" : month_number,
        "cal": cal,
        "current_year": current_year,
    }
        )

def aboutpage(request):
    return render (request,
        'home/aboutpage.html', {})

def contact(request):
    return render (request,
        'home/contact.html', {})

def gallery(request):
    return render (request,
        'home/gallery.html', {})

def musicdvds(request):
    return render (request,
        'home/musicdvds.html', {})















