from state_monitor.models import APIStatus, Application, API
from rest_framework import serializers


class APIStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APIStatus
        fields = (
            'status_id',
            'full_url',
            'check_time',
            'status',
        )


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = (
            'app_id',
            'name',
        )


class APISerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = API
        fields = (
            'api_id',
            'name',
            'status',
        )
