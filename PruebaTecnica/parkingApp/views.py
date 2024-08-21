from django.shortcuts import render
from .models import Parking

# Create your views here.
def parking_view(request):
    parking = Parking.objects.first()
    context = {
        'total_spaces': parking.total_spaces,
        'available_spaces': parking.available_spaces,
    }
    return render(request, 'parking.html', context)