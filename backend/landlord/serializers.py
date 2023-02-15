from rest_framework import serializers
from django.contrib.auth.models import User, Group

from .models import Property

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'id',
            'type',
            'address',
            'get_absolute_url',
            'description',
            'price',
            'get_image',
            'get_thumbnail'
        ]