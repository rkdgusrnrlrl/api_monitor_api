from .models import APICallLog, APIMonitorRequest
from rest_framework import viewsets
from .serializers import APICallLogSerializer, APIMonitorRequestSerializer
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response


class APICallLogViewSet(viewsets.ModelViewSet):
    queryset = APICallLog.objects.all().order_by('-created_at')
    serializer_class = APICallLogSerializer


class APIMonitorRequestViewSet(viewsets.ModelViewSet):
    queryset = APIMonitorRequest.objects.all().order_by('-created_at')
    serializer_class = APIMonitorRequestSerializer

    @detail_route(methods=['post'])
    def run_task(self, request, pk=None):
        api_request = APIMonitorRequest.objects.get(pk=pk)
        serializer = self.get_serializer(api_request)
        return Response(serializer.data)