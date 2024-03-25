from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import User


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password']

    def is_valid(self, *, raise_exception=False):
        email = self.context['request'].data.get('email')
        try:
            user = User.objects.get(email=email)
            if user.is_verified:
                raise ValidationError({'email': 'Пользователь уже зарегистрирован'})
            return True
        except User.DoesNotExist:
            return True


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password']

    def is_valid(self, *, raise_exception=False):
        email = self.context['request'].data.get('email')
        password = self.context['request'].data.get('password')
        try:
            user = User.objects.get(email=email)
            if user.is_verified:
                if user.check_password(password):
                    return True
                else:
                    raise ValidationError({'password': 'Неверный пароль'})
            else:
                raise ValidationError({'email': 'Пользователь не подтвержден'})
        except User.DoesNotExist:
            raise ValidationError('Email не зарегистрирован')
