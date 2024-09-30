from django.shortcuts import render, redirect
from .forms import VehicleRegistrationForm  # You'll need to create this form
from .models import Vehicle

def register_vehicle(request):
    if request.method == 'POST':
        form = VehicleRegistrationForm(request.POST)
        if form.is_valid():
            vehicle = form.save()  # Create a new Vehicle object
            return redirect('success_page')  # Redirect to a success page
    else:
        form = VehicleRegistrationForm()
    return render(request, 'register_vehicle.html', {'form': form})
        
def index(request):
    return render(request, 'index.html')

def track(request):
    return render(request, 'track.html')

def login(request):
    return render(request, 'lr.html')