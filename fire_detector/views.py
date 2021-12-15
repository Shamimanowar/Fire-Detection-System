from django.shortcuts import render
from .models import FireDetector
from .serializers import ValueSerializer
from rest_framework import generics

# Create your views here.


class ListCreateView(generics.ListCreateAPIView):
    queryset = FireDetector.objects.all()
    serializer_class = ValueSerializer


class RetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FireDetector.objects.all()
    serializer_class = ValueSerializer
    lookup_field = 'id'
