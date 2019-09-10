from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Handover2pm
from .serializers import Handover2pmSerializer

# Create your views here.


# def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")

class Handover2pmViewSet(viewsets.ModelViewSet):
    queryset = Handover2pm.objects.all()
    serializer_class = Handover2pmSerializer