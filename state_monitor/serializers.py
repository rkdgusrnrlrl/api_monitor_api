from state_monitor.models import APIStatus, Application, API
from rest_framework import serializers


class APIStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APIStatus
        fields = (
            'status_id',
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
    last_status = APIStatusSerializer()

    class Meta:
        model = API
        fields = (
            'api_id',
            'name',
            'last_status',
        )
