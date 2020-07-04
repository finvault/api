from django.shortcuts import render
from django.http import JsonResponse

def service_view(request):
    data = {
        'name': 'jason',
        'age': 21
    }
    return JsonResponse(data)
