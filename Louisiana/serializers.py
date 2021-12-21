from django.contrib.auth.models import User, Group
from Louisiana.models import Slavetransactions
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class SlaveTransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Slavetransactions
        fields = ['index','name','year','docdate','seller','buyer']