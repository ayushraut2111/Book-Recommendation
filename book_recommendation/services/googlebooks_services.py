import requests
from django.conf import settings
import json


class GoogleBooksService:
    def __init__(self) -> None:
        self.base_url = settings.GOOGLE_BOOKS_APIS_CONF.API_URL
        self.api_key = settings.GOOGLE_BOOKS_APIS_CONF.API_KEY

    def make_request(self, endpoint, method="GET", params={}, data={}):
        url = f'{self.base_url}/{endpoint}?key={self.api_key}'

        headers = {}

        dump_methods = ["POST", "PUT", "PATCH"]

        if method in dump_methods:
            data = json.dumps(data)

        response = requests.request(
            method=method, url=url, params=params, data=data, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print("google books api call error: ",
                  response.json(), response.status_code)
            return None
