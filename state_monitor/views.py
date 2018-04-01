from django.shortcuts import render
from .models import APICallLog, APIMonitorRequest
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import APICallLogSerializer, APIMonitorRequestSerializer


class APICallLogViewSet(viewsets.ModelViewSet):
    queryset = APICallLog.objects.all().order_by('-created_at')
    serializer_class = APICallLogSerializer


class APIMonitorRequestViewSet(viewsets.ModelViewSet):
    queryset = APIMonitorRequest.objects.all().order_by('-created_at')
    serializer_class = APIMonitorRequestSerializer