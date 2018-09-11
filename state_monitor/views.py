from .models import APIStatus, Application, API
from rest_framework import viewsets
from .serializers import APISerializer, ApplicationSerializer


class APIStatusVeiwSet(viewsets.ModelViewSet):
    queryset = APIStatus.objects.all()
    serializer_class = APIStatus


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class APIViewSet(viewsets.ModelViewSet):
    serializer_class = APISerializer

    def get_queryset(self):
        return API.objects.filter(application=self.kwargs['application_pk'])
