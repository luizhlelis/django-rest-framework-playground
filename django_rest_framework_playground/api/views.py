from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_rest_framework_playground.api.serializers import UserSerializer, GroupSerializer, ItemSerializer
from django_rest_framework_playground.api.models import Item
from rest_framework.exceptions import APIException

class UniquenessException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Entity has been already created"

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

class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]


# if you want to use the following method yoy must map it on urls.py (ModelViewSet has just created all CRUD methods)
@api_view(['POST'])
def create_item(request):
    serializer = ItemSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    try:
        serializer.save()
    except:
        raise UniquenessException()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
