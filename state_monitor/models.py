from django.db import models

class APICallLog(models.Model):
    call_id = models.AutoField(primary_key=True)
    api_name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    full_url = models.TextField()
    req_body = models.TextField()
    res_body = models.TextField()
    res_second = models.FloatField()