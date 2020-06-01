from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'TextGroups', views.TextGroupViewSet)
router.register(r'TextGroupMember', views.TextGroupMemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
]
