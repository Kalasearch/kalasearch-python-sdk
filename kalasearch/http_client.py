import requests


class HttpClient():
    config = None
    headers = {}

    def __init__(self, config):
        self.config = config
        self.headers = {
            "X-Kalasearch-Id": self.config.appId,
            "X-Kalasearch-Key": self.config.apiKey,
            "Content-Type": "application/json"
        }

    def send_request(self, http_method, path, body=None):
        endpoint = self.config.domain + "/" + path
        if body is None:
            request = http_method(endpoint, headers=self.headers)
        else:
            request = http_method(endpoint, headers=self.headers, json=body)
        return request.json()

    def get(self, path):
        return self.send_request(requests.get, path)

    def post(self, path, body=None):
        return self.send_request(requests.post, path, body)
