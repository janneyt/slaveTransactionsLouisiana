from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from Louisiana.models import SlaveTransactions
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, SlaveTransactionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse
from django.core.exceptions import FieldError




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

    '''
    The database table was taken from a Pandas dataframe, hence some of my naming conventions.
    The extra action listed here is meant to provide a "column", or quite literally all of the 
    values in the SQL table by the column.
    '''
    @action(detail=False)
    def columns(self, request):
        '''
        Returns the desired column, with an option for distinct values
        '''
        desired_field = request.query_params.get('field')
        distinct = request.query_params.get('distinct')
        try:
            values = SlaveTransactions.objects.all ().values_list(desired_field, flat=True)
            if distinct:
                values = values.distinct ( desired_field )
            return Response ( values )
        except ValueError:
            return JsonResponse({"column":"not found"})
        except SlaveTransactions.DoesNotExist:
            return JsonResponse({"Slave Transactions":"Model does not exist in database, check database connection and existence"})
        except FieldError:
            field = "The field " + desired_field + " does not exist"
            return JsonResponse({"Existence of field":field})


