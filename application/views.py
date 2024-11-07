

from django.shortcuts import render, redirect,get_object_or_404
from .forms import CustomerCreationForm,CustomerUpdateForm
from django.contrib.auth import login

from .models import Itinerary,Activity

def create_customer(request):
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomerCreationForm()

    return render(request, 'create_customer.html', {'form': form})

def customer_detail(request):
    customer = request.user
    return render(request, 'customer_detail.html', {'customer': customer})


def edit_customer(request):
    if request.method == 'POST':
        form = CustomerUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('customer_detail')
    else:
        form = CustomerUpdateForm(instance=request.user)

    return render(request, 'edit_customer.html', {'form': form})


from .forms import DestinationForm

def create_destination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('destination_list')  # Redirect to the destination list view or home
    else:
        form = DestinationForm()  # An unbound form

    return render(request, 'create_destination.html', {'form': form})


from .models import Destination

def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'destination_list.html', {'destinations': destinations})

def edit_destination(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == "POST":
        form = DestinationForm(request.POST, instance=destination)
        if form.is_valid():
            form.save()
            return redirect('destination_list')
    else:
        form = DestinationForm(instance=destination)
    return render(request, 'edit_destination.html', {'form': form})

def delete_destination(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == "POST":
        destination.delete()
        return redirect('destination_list')
    return render(request, 'delete_destination.html', {'destination': destination})


from .forms import ItineraryForm

def create_itinerary(request):
    if request.method == 'POST':
        form = ItineraryForm(request.POST)
        if form.is_valid():
            itinerary = form.save(commit=False)
            itinerary.user = request.user
            itinerary.save()
            return redirect('itineraries_by_destination',destination_id=itinerary.destination.pk)
    else:
        form = ItineraryForm()

    return render(request, 'create_itinerary.html', {'form': form})

from .forms import ActivityForm


def create_activity(request, itinerary_id):
    itinerary = get_object_or_404(Itinerary, id=itinerary_id)
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.itinerary = itinerary
            activity.save()
            return redirect('activities_by_itinerary', itinerary_id=itinerary_id)
    else:
        form = ActivityForm()

    return render(request, 'create_activity.html', {'form': form, 'itinerary': itinerary})

def edit_activity(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('activities_by_itinerary', itinerary_id=activity.itinerary.id)

    else:
        form = ActivityForm(instance=activity)
    return render(request, 'edit_activity.html', {'form': form, 'activity': activity})

def delete_activity(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    itinerary_id = activity.itinerary.id
    if request.method == 'POST':
        activity.delete()
        return redirect('activities_by_itinerary', itinerary_id=itinerary_id)
    return render(request, 'delete_activity.html', {'activity': activity})


from .models import Itinerary, Destination

def itineraries_by_destination(request, destination_id):
    destination = get_object_or_404(Destination, pk=destination_id)
    itineraries = Itinerary.objects.filter(destination=destination).order_by('-start_date')
    return render(request, 'itineraries_by_destination.html', {
        'destination': destination,
        'itineraries': itineraries
    })


def activities_by_itinerary(request, itinerary_id):
    itinerary = get_object_or_404(Itinerary, pk=itinerary_id)
    activities = Activity.objects.filter(itinerary=itinerary)
    return render(request, 'activities_by_itinerary.html', {
        'itinerary': itinerary,
        'activities': activities
    })