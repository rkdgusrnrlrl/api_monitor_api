from django.db import models
import json

METHOD_CHOICES = (
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('DELETE', 'DELETE'),
    )

class APICallLog(models.Model):
    call_id = models.AutoField(primary_key=True)
    api_name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    full_url = models.TextField()
    req_body = models.TextField()
    res_body = models.TextField()
    res_second = models.FloatField()


class APIStatus(models.Model):
    API_STATUS_CHOICES = (
        ('SUCCESS', '성공'),
        ('FAIL', '실패'),
    )
    status_id = models.AutoField(primary_key=True)
    api_name = models.CharField(max_length=100)
    method = models.CharField(
        max_length=6,
        choices=METHOD_CHOICES,
        default="GET"
    )
    full_url = models.TextField()
    check_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=API_STATUS_CHOICES)


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
    req_url = models.CharField(max_length=100)
    req_body = models.TextField(blank=True)
    req_headers = models.TextField(blank=True)
    req_method = models.CharField(
        max_length=6,
        choices=REQ_METHOD_CHOICES,
        default="GET"
    )
    req_qs = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)

    def get_headers(self):
        try:
            return json.loads(self.req_headers)
        except ValueError:
            return {}

    def get_body(self):
        try:
            return json.loads(self.req_body)
        except ValueError:
            return {}

    def set_req_body(self, req_body):
        json.load(req_body)
        self.req_body = req_body
