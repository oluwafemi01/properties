from django.shortcuts import render
from properties.models import properties
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import PropertiesSerializer
# Create your views here.

class all(generics.ListAPIView):
    queryset = properties.objects.all()
    serializer_class = PropertiesSerializer

class details(generics.RetrieveAPIView):
    queryset = properties.objects.all()
    serializer_class = PropertiesSerializer

