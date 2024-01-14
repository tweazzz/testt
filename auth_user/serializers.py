from rest_framework import serializers
from .models import User
from django.utils.translation import gettext_lazy as _
from djoser.serializers import TokenCreateSerializer
from rest_framework import serializers
from djoser.serializers import TokenSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext as _



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'school', 'date_joined', 'is_active', 'is_staff')


