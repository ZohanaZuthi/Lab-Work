from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

hotels_data = [
    {"id": 1, "name": "City Hotel", "location": "New York"},
    {"id": 2, "name": "Beach Resort", "location": "California"},
]

def home(request):
    return HttpResponse("<h2>Hotel Booking API Running</h2><p>Use /hotels/ or /book/</p>")

def hotels(request):
    return JsonResponse(hotels_data, safe=False)

@csrf_exempt
def book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        return JsonResponse({"message": "Booking Created", "payload": data})
    return JsonResponse({"error": "POST only"}, status=400)
