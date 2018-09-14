from django.db import models


METHOD_CHOICES = (
    ('GET', 'GET'),
    ('POST', 'POST'),
    ('PUT', 'PUT'),
    ('DELETE', 'DELETE'),
)


class Application(models.Model):
    app_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    base_url = models.TextField()


class API(models.Model):
    api_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    full_url = models.TextField()
    method = models.CharField(max_length=6, choices=METHOD_CHOICES, default="GET")
    application = models.ForeignKey(Application, on_delete=models.CASCADE)

    @property
    def last_status(self):
        return self.apistatus_set.all().order_by('-check_time').first()


class APIStatus(models.Model):
    API_STATUS_CHOICES = (
        ('SUCCESS', '성공'),
        ('FAIL', '실패'),
    )
    status_id = models.AutoField(primary_key=True)
    check_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=API_STATUS_CHOICES)
    api = models.ForeignKey(API, on_delete=models.CASCADE)
