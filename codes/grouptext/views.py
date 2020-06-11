from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

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


@api_view(['POST'])
def add_group_member(request, group_id):

    # look up textgroup from textgroup_id
    text_group = TextGroup.objects.get(id=group_id)

    text_group_member = TextGroupMember()
    text_group_member.member_name = request.data.get("member_name")
    text_group_member.member_phone = request.data.get("member_phone")
    text_group_member.text_group = text_group
    text_group_member.save()

    return Response({'id': text_group_member.id})
