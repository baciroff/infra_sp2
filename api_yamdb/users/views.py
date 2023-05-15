from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import GetTokenSerializer, UserSerializer


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    new_user = User.objects.get(username=request.data['username'])
    code = default_token_generator.make_token(new_user)
    send_mail(
        'Confirmation code for ' + request.data['username'],
        code,
        'from@example.com',
        [request.data['email']],
        fail_silently=False,
    )
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def token(request):
    serializer = GetTokenSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.get(
            username=request.data['username']
        )
        refresh = RefreshToken.for_user(user)

        return Response(
            {'token': str(refresh.access_token)},
            status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
