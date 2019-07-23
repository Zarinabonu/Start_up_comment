from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.permissions import AllowAny
from api.serializers import StartupsSerializer, StartupStatusesSerializer, StartupFilesSerializer, StartupCommentSerializer ,StartupReplySerializer
from startups.models import Startups, StartupStatuses, StartupFiles , Comments , StartupReply

from rest_framework.generics import CreateAPIView , ListAPIView


class StartupsAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = StartupsSerializer

    def get_queryset(self):
        return Startups.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class StartupStatusesAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = StartupStatusesSerializer

    def get_queryset(self):
        return StartupStatuses.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class StartupFilesAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = StartupFilesSerializer

    def get_queryset(self):
        return StartupFiles.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class StartupCommentAPIView(generics.CreateAPIView):  
    queryset = Comments.objects.all()
    serializer_class = StartupCommentSerializer

class StartupCommentList(generics.ListAPIView):   
    serializer_class =  StartupCommentSerializer
    model = Comments
    queryset = Comments.objects.all()

class StartupReplyAPIView(generics.CreateAPIView):
    queryset = StartupReply.objects.all()  
    serializer_class = StartupReplySerializer

class StartupReplyList(generics.ListAPIView):
    serializer_class = StartupReplySerializer 
    model = StartupReply
    queryset = StartupReply.objects.all()

    

