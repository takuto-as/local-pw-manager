from django.contrib.auth.models import User, Group
from rest_framework import serializers
from password_manager.models import LoginModel

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class LoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LoginModel
        fields = ['name', 'user_name', 'password', 'url', 'created', 'updated', 'active', 'description']