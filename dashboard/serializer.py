
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from .exception import IncorrectAuthCredentials

class LoginSerializer(serializers.Serializer):
    """This is the serializer used for logging in user"""
    email = serializers.EmailField(max_length=256, required=True)
    password = serializers.CharField(required=True, min_length=5)
    username = serializers.SerializerMethodField()

    class Meta:
        model = User

    def get_username(self,obj):
        try:
           return User.objects.get(email=obj['email']).username
        except:
            raise IncorrectAuthCredentials(detail="Incorrect authentication credentials", code=401)