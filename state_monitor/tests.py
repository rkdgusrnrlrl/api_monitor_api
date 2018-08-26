import pytest
from .models import APICallLog, APIStatus
import datetime
import pytz


@pytest.mark.django_db
def test_create_api_status_should_be_set_time():
    before_insert_time = pytz.utc.localize(datetime.datetime.utcnow())
    api_status = APIStatus.objects.create(
        api_name="사용자를 등록하는 API",
        full_url="http://api.dakbutfly.me/users",
        method="GET",
        status="SUCCESS"
    )
    after_insert_time = pytz.utc.localize(datetime.datetime.utcnow())
    assert api_status.check_time > before_insert_time
    assert api_status.check_time < after_insert_time
