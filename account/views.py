from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import authentication_classes, api_view, permission_classes

from account import service


# Create your views here.
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([])
def register(request):
    # data = User.objects.all()
    return service.register(request)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([])
def login(request, format=None):
    return service.login(request)