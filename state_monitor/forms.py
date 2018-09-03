from django.forms import ModelForm
from state_monitor.models import API, APIStatus

class APIForm(ModelForm):
    class Meta:
        model = API
        fields = ('name', 'full_url', 'method',)


class APIStatusForm(ModelForm):
    class Meta:
        model = APIStatus
        fields = ('status',)