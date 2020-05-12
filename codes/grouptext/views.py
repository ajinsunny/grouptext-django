from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .serializers import TextGroupSerializer
from .models import TextGroup

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

class TextGroupViewSet(viewsets.ModelViewSet):
    queryset = TextGroup.objects.all().order_by('name')
    serializer_class = TextGroupSerializer
    

