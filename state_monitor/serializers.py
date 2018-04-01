from .models import APICallLog, APIMonitorRequest
from rest_framework import serializers

class APICallLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APICallLog
        fields = ('call_id','api_name',
                  'created_at','status',
                  'full_url','req_body',
                  'res_body','res_second','url')


class APIMonitorRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APIMonitorRequest
        fields = (
            'api_req_id',
            'api_name',
            'api_base_url',
            'req_url',
            'req_body',
            'req_headers',
            'req_method',
            'req_qs',
        )

