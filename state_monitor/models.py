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


class API(models.Model):
    api_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    full_url = models.TextField()
    method = models.CharField(max_length=6, choices=METHOD_CHOICES, default="GET")
    application = models.ForeignKey(Application, on_delete=models.CASCADE)

    @property
    def status(self):
        return self.apistatus_set.all().order_by('check_time').first()


class APIStatus(models.Model):
    API_STATUS_CHOICES = (
        ('SUCCESS', '성공'),
        ('FAIL', '실패'),
    )
    status_id = models.AutoField(primary_key=True)
    check_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=API_STATUS_CHOICES)
    api = models.ForeignKey(API, on_delete=models.CASCADE)


def validate_method_choice(sender, instance, **kwargs):
    valid_methods = [t[0] for t in METHOD_CHOICES]
    if instance.method not in valid_methods:
        from django.core.exceptions import ValidationError
        raise ValidationError(
            'API Method "{}" is not one of the permitted values: {}'.format(
                instance.method,
               ', '.join(valid_methods)))


def validate_status_choice(sender, instance, **kwargs):
    valid_status = [t[0] for t in sender.API_STATUS_CHOICES]
    if instance.status not in valid_status:
        from django.core.exceptions import ValidationError
        raise ValidationError(
            'API Method "{}" is not one of the permitted values: {}'.format(
                instance.status,
               ', '.join(valid_status)))


models.signals.pre_save.connect(validate_method_choice, sender=API)
models.signals.pre_save.connect(validate_status_choice, sender=APIStatus)