# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import requests


@shared_task
def call_request(request):
    body = request.get_body()
    headers = request.get_header()
    api_base_url = request.api_base_url
    req_url = request.req_url
    req_method = request.req_method

    try:
        r = call_api(api_base_url, req_url, body, headers, req_method)
        if r is None:
            return

        res_sec = r.elapsed.total_seconds()
        res_data = r.json()
        res_data['res_sec'] = res_sec
        return res_data
    except Exception as e:
        print(e)

def call_api(api_base_url, api_url, body, headers, method):
    if method is 'GET':
        return requests.post(api_base_url + api_url, data=body, headers=headers)
    elif method is 'POST':
        return requests.post(api_base_url + api_url, data=body, headers=headers)
    elif method is 'PUT':
        return requests.post(api_base_url + api_url, data=body, headers=headers)
    elif method is 'DELETE':
        return requests.post(api_base_url + api_url, data=body, headers=headers)
    else:
        return None