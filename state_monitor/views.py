from .models import APIStatus, Application, API
from rest_framework import viewsets
from .serializers import APISerializer, ApplicationSerializer, APIStatusSerializer


class APIStatusVeiwSet(viewsets.ModelViewSet):
    queryset = APIStatus.objects.all()
    serializer_class = APIStatusSerializer

    def get_queryset(self):
        return APIStatus.objects.filter(api=self.kwargs['api_pk'])


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class APIViewSet(viewsets.ModelViewSet):
    serializer_class = APISerializer

    def get_queryset(self):
        return API.objects.filter(application=self.kwargs['application_pk'])