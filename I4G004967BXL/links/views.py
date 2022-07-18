from django.shortcuts import render
from rest_framework import viewsets
from .models import Link
from .serializer import LinkSerializer
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from django.utils import timezone


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime 

# Create your views here.


class PostListApi(ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostCreateApi(CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostDetailApi(RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostUpdateApi(UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostDeleteApi(DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
class  ActiveLinkView(APIView):
    """
    Returns a list of all active (publicly accessible) links
    """
    def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        qs = Link.public.all()
        data = LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)

class RecentLinkView(APIView):
    """
    Returns a list of recently created active links
    """
    def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        seven_days_ago = timezone.now() - datetime.timedelta(days=7)
        qs = Link.public.filter(created__gte = seven_days_ago)
        data = LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)
