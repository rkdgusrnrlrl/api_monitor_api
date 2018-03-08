from django.shortcuts import render
from .models import APICallLog
from rest_framework import viewsets
from .serializers import APICallLogSerializer

class APICallLogViewSet(viewsets.ModelViewSet):
    queryset = APICallLog.objects.all().order_by('-created_at')
    serializer_class = APICallLogSerializer
