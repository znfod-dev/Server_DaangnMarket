import os

import firebase_admin
from firebase_admin import auth, credentials
from django.contrib.auth import get_user_model
from rest_framework import serializers, status
from rest_framework.response import Response

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)

cred = credentials.Certificate(f"{ROOT_DIR}/serviceAccountKey.json")
default_app = firebase_admin.initialize_app(cred)

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(allow_empty_file=True)
    Authorization = serializers.SerializerMethodField(method_name='get_authorization')

    class Meta:
        model = User
        fields = [
            'uid',
            'avatar',
            'phone',
            'created',
            'updated',
            'username',
            'Authorization',
        ]

    def get_authorization(self, obj):
        return f'Token {obj.auth_token}'


class LoginSerializer(serializers.Serializer):
    id_token = serializers.CharField()
    user = UserSerializer()

    class Meta:
        read_only_fields = ['user', ]
        extra_kwargs = {
            'id_token': {'write_only': True},
        }

    def validate_id_token(self, value):
        try:
            decoded_token = auth.verify_id_token(value)
            uid = decoded_token['uid']
            user = User.objects.get_or_none(uid=uid)
            if not user:
                raise ValueError
        except ValueError:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
