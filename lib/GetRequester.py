import json

import requests


class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(url=self.url)
        return response.content

    def load_json(self):
        res_json = requests.get(url=self.url)
        return res_json.json()
