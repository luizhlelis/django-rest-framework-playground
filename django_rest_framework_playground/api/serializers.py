from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django_rest_framework_playground.api.models import Item


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('category', 'subcategory', 'name', 'amount')

class ErrorDetailsSerializer(serializers.Serializer):
    field_related_errors = serializers.JSONField(required=False)
    requestId = serializers.UUIDField()
    msg = serializers.CharField(required=False)

class GlobalErrorSerializer(serializers.Serializer):
    error = ErrorDetailsSerializer()
    status_code = serializers.IntegerField()
    type = serializers.CharField()