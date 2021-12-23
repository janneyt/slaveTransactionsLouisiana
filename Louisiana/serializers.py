from django.contrib.auth.models import User, Group
from Louisiana.models import SlaveTransactions
from rest_framework import serializers


class UserSerializer ( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer ( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Group
        fields = ['url', 'name']


class SlaveTransactionSerializer ( serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SlaveTransactions
        fields = '__all__'


