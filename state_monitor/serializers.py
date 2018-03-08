from .models import APICallLog
from rest_framework import serializers

class APICallLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APICallLog
        fields = ('call_id','api_name',
                  'created_at','status',
                  'full_url','req_body',
                  'res_body','res_second','url')

