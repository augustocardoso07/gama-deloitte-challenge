from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Member, Post, Service
from .serializers import MemberSerializer, PostSerializer, ServiceSerializer


class MemberView(viewsets.ModelViewSet):
    """
    retrieve:
        Retorna um membro da equipe.

    list:
        Retornar uma lista com todos os membros da equipe

    create:
        Cria um novo membro da equipe.

    delete:
        Exluir um membro existente da equipe

    update:
        Atualiza um membro da equipe.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']


class PostView(viewsets.ModelViewSet):
    """
    retrieve:
        Retorna um post.

    list:
        Retornar todos os posts publicados

    create:
        Cria um novo post.

    delete:
        Exluir um post

    update:
        Atualiza um post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']


class ServiceView(viewsets.ModelViewSet):
    """
    retrieve:
        Retorna um serviço.

    list:
        Retornar todos os serviços

    create:
        Cria um novo serviço.

    delete:
        Exluir um serviço

    update:
        Atualiza um serviço.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']
