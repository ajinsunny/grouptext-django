from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TextGroupSerializer, TextGroupMemberSerializer
from .serializers import TextQuestionSerializer
from .models import TextGroup, TextGroupMember, TextQuestion

# Create your views here.


def index(request):
    return HttpResponse("Hello World")


class TextGroupViewSet(viewsets.ModelViewSet):
    queryset = TextGroup.objects.all().order_by('group_name')
    serializer_class = TextGroupSerializer


class TextGroupMemberViewSet(viewsets.ModelViewSet):
    queryset = TextGroupMember.objects.all().order_by('text_group')
    serializer_class = TextGroupMemberSerializer


class TextQuestionMemberSet(viewsets.ModelViewSet):
    queryset = TextQuestion.objects.all().order_by('text_group')
    serializer_class = TextQuestionSerializer


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


@api_view(['GET'])
def get_groups_and_members(request):

    text_groups_members = []
    text_groups = TextGroup.objects.all()
    for text_group in text_groups:
        text_group_info = {
            'group_id': text_group.id,
            'group_name': text_group.group_name,
            'members': [],
        }

        text_group_members = TextGroupMember.objects.filter(
            text_group=text_group).all()

        for text_group_member in text_group_members:
            text_group_info['members'].append({
                'member_name': text_group_member.member_name,
                'member_phone': text_group_member.member_phone,
                'member_id': text_group_member.id,
            })

        text_groups_members.append(text_group_info)

    return Response(text_groups_members)
