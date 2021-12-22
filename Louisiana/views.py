from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from Louisiana.models import SlaveTransactions
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, SlaveTransactionSerializer



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

class TransactionRecordsViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows transaction records to be viewed or edited
    '''
    queryset = SlaveTransactions.objects.all()
    serializer_class = SlaveTransactionSerializer
    permission_classes = [permissions.IsAuthenticated]