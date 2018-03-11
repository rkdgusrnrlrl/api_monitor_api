from django.db import models
import json

class APICallLog(models.Model):
    call_id = models.AutoField(primary_key=True)
    api_name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    full_url = models.TextField()
    req_body = models.TextField()
    res_body = models.TextField()
    res_second = models.FloatField()


class APIMonitorRequest(models.Model):
    REQ_METHOD_CHOICES = (
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('DELETE', 'DELETE'),
    )

    api_req_id = models.AutoField(primary_key=True)
    api_name = models.CharField(max_length=100)
    api_base_url = models.TextField()
    req_body = models.TextField()
    req_method = models.CharField(
        max_length=6,
        choices=REQ_METHOD_CHOICES,
        default="GET"
    )
    req_qs = models.TextField()

    def get_body(self):
        try:
            return json.loads(self.req_body)
        except ValueError:
            return {}

    def set_req_body(self, req_body):
        json.load(req_body)
        self.req_body = req_body

