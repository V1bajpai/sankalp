from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

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

# @api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# # @permission_classes([IsAuthenticated, is_verified])
# @permission_classes([IsAuthenticated])
# def get_profile(request):
#     return ProfileService.get_profile(request)
#
#
# # An API for updating profile details of user.
# @api_view(['POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# # @permission_classes([IsAuthenticated, is_verified])
# def update_profile(request):
#     return ProfileService.update_profile(request)
