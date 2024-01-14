from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework import generics
from djoser.serializers import UserCreateSerializer,TokenCreateSerializer
from rest_framework import viewsets, status,mixins
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework import status


class UserListView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AdminUserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()
        mutable_data['role'] = 'admin'
        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ClientUserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()
        mutable_data['role'] = 'client'
        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



