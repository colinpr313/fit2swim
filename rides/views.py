from django.shortcuts import render, redirect

from .models import Person

# relative import of forms
from .forms import RideForm

# Create your views here.
from .forms import RideForm, NewRideForm


def index(request):

  context = {}

  if "searchoc" in request.GET:
    searchoc = request.GET["searchoc"]
    if searchoc != "":
        context["people"] = Person.objects.filter(
            origination_city__iexact=searchoc) | Person.objects.filter(origination_city__iexact=searchoc)

  if "searchos" in request.GET:
    searchos = request.GET["searchos"]
    if searchos != "":
        context["people"] = Person.objects.filter(
            origination_state__iexact=searchos) | Person.objects.filter(origination_state__iexact=searchos)

  if "searchdc" in request.GET:
    search2 = request.GET["searchdc"]
    if searchdc != "":
        context["people"] = Person.objects.filter(
            destination_city__iexact=searchdc) | Person.objects.filter(destination_city__icontains=searchdc)

  if "searchds" in request.GET:
    searchds = request.GET["searchds"]
    if searchds != "":
        context["people"] = Person.objects.filter(
            destination_state__iexact=searchds) | Person.objects.filter(destination_state__icontains=searchds)


  if "searchdate" in request.GET:
    searchdate = request.GET["searchdate"]
    if searchdate != "":
        context["people"] = Person.objects.filter(
            date__iexact=searchdate) | Person.objects.filter(date__icontains=searchdate)

  if "searchvt" in request.GET:
   searchvt = request.GET["searchvt"]
   if searchvt != "":
       context["people"] = Person.objects.filter(
           vehicle_type__iexact=searchvt) | Person.objects.filter(vehicle_type__icontains=searchvt)

  if "searchpremium" in request.GET:
    searchpremium = request.GET["searchpremium"]
    if searchpremium != "":
        context["people"] = Person.objects.filter(
            premium__iexact=searchpremium) | Person.objects.filter(premium__icontains=searchpremium)

  if "searchpass" in request.GET:
    searchpass = request.GET["searchpass"]
    if searchpass != "":
        context["people"] = Person.objects.filter(
            taking_passengers__iexact=searchvt) | Person.objects.filter(taking_passengers__icontains=searchpass)


  context["form"] = RideForm()


  return render(request, "index_view.html", context)

def create(request):
    context = {}
    context["new_ride_form"] = NewRideForm()

    if request.method == "POST":
        new_ride = NewRideForm(request.POST)
        new_ride.save()
        return redirect('/rides')
    else:
        return render(request, "find_view.html", context)
