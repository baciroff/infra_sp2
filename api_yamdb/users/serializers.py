import re

from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from rest_framework import exceptions, serializers

from .models import User


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=254, required=True)
    username = serializers.CharField(max_length=150, required=True)

    def validate_username(self, data):
        if data == 'me':
            raise exceptions.ValidationError('Недоступное username')
        reg = re.compile(r'^[\w.@+-]+')
        if not reg.match(data):
            raise exceptions.ValidationError('Неккоректное username')
        return data

    def validate(self, data):
        if User.objects.filter(
                username=data['username']).exclude(
                    email=data['email']).exists():
            raise exceptions.ParseError(
                'Пользователь с таким username уже существует')
        if User.objects.filter(
                email=data['email']).exclude(
                    username=data['username']).exists():
            raise exceptions.ParseError(
                'Пользователь с таким email уже существует')
        return data

    def create(self, validated_data):
        user, created = User.objects.get_or_create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.save()
        return user


class GetTokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=True)
    confirmation_code = serializers.CharField(required=True)

    def validate_username(self, data):
        reg = re.compile(r'^[\w.@+-]+')
        if not reg.match(data):
            raise exceptions.ValidationError('Некорректное username')
        return data

    def validate(self, data):
        user = get_object_or_404(
            User,
            username=data['username'],
        )
        if not default_token_generator.check_token(user,
                                                   data['confirmation_code']):
            raise exceptions.ParseError('Неверный код подтверждения')
        return data
