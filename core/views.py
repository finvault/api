from django.shortcuts import render
from django.http import JsonResponse

def service_view(request):
    data = {
        'title': 'jason',
        'description': 21
    }
    return JsonResponse(data)
