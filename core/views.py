from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ServiceSerializer
from .models import Service
from rest_framework import generics
from rest_framework import mixins

class serviceView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

# def service_view(request):
#     data = {
#         'title': 'jason',
#         'description': 21
#     }
#     return JsonResponse(data)
