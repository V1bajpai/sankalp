import binascii
import os
import traceback

from django.contrib.auth.models import User
from fastapi_admin.i18n import _
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from account.models import UserDetail, SignupValidationToken
from rest_framework.views import APIView


def register(request):
    try:
        if 'email' not in request.data:
            return Response({"message": _("Email field is required.")}, status=status.HTTP_400_BAD_REQUEST)
        elif 'name' not in request.data or (len(request.data['name']) <= 0):
            return Response({"message": _("Name field is required.")}, status=status.HTTP_400_BAD_REQUEST)
        elif 'password' not in request.data or (len(request.data['password']) <= 0):
            return Response({"message": _("Password field is required.")}, status=status.HTTP_400_BAD_REQUEST)
        elif 'country_code' not in request.data or (len(request.data['country_code']) <= 0):
            return Response({"message": _("country_code field is required.")}, status=status.HTTP_400_BAD_REQUEST)
        elif 'phone' not in request.data:
            return Response({"message": _("phone field is required.")}, status=status.HTTP_400_BAD_REQUEST)
        elif 'gender' not in request.data:
            return Response({"message": _("gender type field is required.")}, status=status.HTTP_400_BAD_REQUEST)


        user = User(
            email=request.data['email'],
            username=request.data['name'],
        )
        user.set_password(request.data['password'])
        user.save()

        user_detail = UserDetail(
            user=user,
            name=request.data['name'],
            email=request.data['email'],
            country_code=request.data['country_code'],
            phone=request.data['phone'],
            gender=request.data['gender'],
        )
        user_detail.save()

        token = generate_token()
        signup_validation_token = SignupValidationToken(
            user=user,
            token=token
        )
        signup_validation_token.save()

        return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        traceback.print_exc()
        return Response({"message": _("We encountered an error. Please try after sometime.")},
                        status=status.HTTP_400_BAD_REQUEST)

def generate_token():
    token = binascii.hexlify(os.urandom(20)).decode()
    return token


def login(request, format=None):
    global language
    try:
        if 'email' not in request.data or (len(request.data['email']) <= 0):
            return Response({"message": _("Email field is required")}, status= status.HTTP_401_UNAUTHORIZED)
        elif 'password' not in request.data or (len(request.data['password']) <= 0):
            return Response({"message": _("Password field is required")}, status= status.HTTP_401_UNAUTHORIZED)
        email = request.data['email']
        email = str(email).strip()
        password = request.data['password']
        password = str(password).strip()
        print('email= ', email, "password= ",password)
        user = User.objects.filter(email__iexact=email).first()
        print('user= ',user)
        if user is not None:
            check_password = user.check_password(password)
            if check_password:
                user_detail = UserDetail.objects.get(user=user)
                if not user_detail:
                    return Response({"message": _(
                        "Sorry, we could not find a user associated with this email, Please Sign up to continue.")},
                                    status=status.HTTP_400_BAD_REQUEST)



                content = {
                    'token': Token.objects.get_or_create(user=user)[0].key,
                    'name': user_detail.name,
                    'email': user_detail.email,
                    }
                user.save()

            else:
                return Response({"message": _("Email or password is incorrect.")}, status= status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": _("Sorry, we could not find a user associated with this email, Please Sign up to continue.")}, status= status.HTTP_400_BAD_REQUEST)
        return Response({'content':content, 'msg':'Login Success'}, status=status.HTTP_200_OK)
    except Exception as e:
        traceback.print_exc()
        return Response({"message": _("We encountered an error. Please try after sometime.")},
                        status=status.HTTP_400_BAD_REQUEST)



