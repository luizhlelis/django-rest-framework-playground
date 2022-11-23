from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_rest_framework_playground.api.serializers import UserSerializer, GroupSerializer
from django_rest_framework_playground.api.models import Item
from django_rest_framework_playground.api.serializers import ItemSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['POST'])
def create_item(request):
    serializer = ItemSerializer(data=request.data)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
