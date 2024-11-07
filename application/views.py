

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

