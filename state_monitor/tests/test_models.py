import pytest
from state_monitor.models import Application, API,APIStatus
from django.core.exceptions import ValidationError

@pytest.mark.django_db
def test_create_application():
    app_name = 'hello123'
    app = Application.objects.create(name=app_name)
    assert app.name == app_name


@pytest.mark.django_db
def test_create_api():
    app_name = 'hello123'
    app = Application.objects.create(name=app_name)

    api_name = '사용자 등록 API'
    api = API.objects.create(name=api_name, full_url='http://api.dakbutfly.me/user', method='POST', application=app)
    assert api_name == api.name


@pytest.mark.django_db
def test_when_wrong_method_should_be_fail():
    with pytest.raises(ValidationError):
        app_name = 'hello123'
        app = Application.objects.create(name=app_name)

        api_name = '사용자 등록 API'
        api = API.objects.create(name=api_name, full_url='http://api.dakbutfly.me/user', method='SHUT', application=app)


@pytest.mark.django_db
def test_create_api_status():
    app_name = 'hello123'
    app = Application.objects.create(name=app_name)

    api_name = '사용자 등록 API'
    api = API.objects.create(name=api_name, full_url='http://api.dakbutfly.me/user', method='POST', application=app)

    api_status = APIStatus.objects.create(api=api, status='SUCCESS')
    assert api_status.status == 'SUCCESS'


@pytest.mark.django_db
def test_when_wrong_status_should_be_raise_validation_error():
    with pytest.raises(ValidationError):
        app_name = 'hello123'
        app = Application.objects.create(name=app_name)

        api_name = '사용자 등록 API'
        api = API.objects.create(name=api_name, full_url='http://api.dakbutfly.me/user', method='POST', application=app)

        api_status = APIStatus.objects.create(api=api, status='WRONG')