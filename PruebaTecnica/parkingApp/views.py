from django.http import JsonResponse
from .models import Parking
from django.utils import timezone
from django.shortcuts import render
from django.db import models
import logging

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'parking.html')

def parking_info(request):
    try:
        total_spaces = Parking.objects.aggregate(total=models.Sum('total_spaces'))['total'] or 0
        available_spaces = Parking.objects.aggregate(available=models.Sum('available_spaces'))['available'] or 0
        data = {
            'total_spaces': total_spaces,
            'available_spaces': available_spaces,
            'updated_at': timezone.now().isoformat()
        }
        return JsonResponse(data)
    except Exception as e:
        logger.error(f"Error fetching parking info: {e}", exc_info=True)
        return JsonResponse({'error': 'Internal Server Error'}, status=500)