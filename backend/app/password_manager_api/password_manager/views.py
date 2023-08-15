from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from password_manager.serializers import UserSerializer, GroupSerializer
from password_manager.serializers import LoginSerializer
from password_manager.models import LoginModel

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = [permissions.IsAuthenticated]

class LoginViewSet(viewsets.ModelViewSet):
    queryset = LoginModel.objects.all().filter(active=True)
    serializer_class = LoginSerializer

    