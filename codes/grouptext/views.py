from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .serializers import TextGroupSerializer, TextGroupMemberSerializer
from .models import TextGroup, TextGroupMember

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

class TextGroupViewSet(viewsets.ModelViewSet):
    queryset = TextGroup.objects.all().order_by('group_name')
    serializer_class = TextGroupSerializer

class TextGroupMemberViewSet(viewsets.ModelViewSet):
    queryset = TextGroupMember.objects.all().order_by('text_group')
    serializer_class = TextGroupMemberSerializer



