from django.shortcuts import render
from rest_framework import viewsets
from .models import Member, Post, Service
from .serializers import MemberSerializer, PostSerializer, ServiceSerializer


class MemberView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
