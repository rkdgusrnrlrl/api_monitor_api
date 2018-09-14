import pytest
from state_monitor.models import Application, API, APIStatus


@pytest.mark.django_db
def test_create_application():
    app_name = 'hello123'
    app = Application.objects.create(name=app_name, base_url="https://api.dakbutfly.me")
    assert app.name == app_name


@pytest.mark.django_db
def test_create_api():
    app_name = 'hello123'
    app = Application.objects.create(name=app_name, base_url="https://api.dakbutfly.me")

    api_name = '사용자 등록 API'
    api = API.objects.create(name=api_name, api_url='/user', method='POST', application=app)
    assert api_name == api.name
    assert 'POST' == api.method


@pytest.mark.django_db
def test_api_full_url_should_be_api_url_with_base_url():
    app_name = 'hello123'
    app = Application.objects.create(name=app_name, base_url="https://api.dakbutfly.me")

    api_name = '사용자 등록 API'
    api = API.objects.create(name=api_name, api_url='/user', method='POST', application=app)

    assert app.base_url + api.api_url == api.full_url


@pytest.mark.django_db
def test_create_api_status():
    app_name = 'hello123'
    app = Application.objects.create(name=app_name, base_url="https://api.dakbutfly.me")

    api_name = '사용자 등록 API'
    api = API.objects.create(name=api_name, api_url='/user', method='POST', application=app)

    api_status = APIStatus.objects.create(api=api, status='SUCCESS')
    assert api_status.status == 'SUCCESS'


@pytest.mark.django_db
def test_when_save_two_status_api_status_should_be_last_status():
    app_name = 'hello123'
    app = Application.objects.create(name=app_name, base_url="https://api.dakbutfly.me")

    api_name = '사용자 등록 API'
    api = API.objects.create(name=api_name, api_url='/user', method='POST', application=app)

    APIStatus.objects.create(api=api, status='FAIL')
    APIStatus.objects.create(api=api, status='SUCCESS')

    assert 'SUCCESS' == api.last_status.status

