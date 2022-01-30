from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Member, Post, Service
from .serializers import MemberSerializer, PostSerializer, ServiceSerializer


class MemberView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
