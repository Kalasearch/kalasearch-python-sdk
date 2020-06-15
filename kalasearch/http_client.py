import requests


class HttpClient():
    config = None
    headers = {}

    def __init__(self, config):
        self.config = config
        self.headers = {
            "apiKey": self.config.apiKey,
            "appId": self.config.appId,
            "Content-Type": "application/json"
        }

    def send_request(self, http_method, path, body=None):
        endpoint = self.config.domain + "/" + path
        print("endpoint = " + endpoint)
        if body is None:
            request = http_method(endpoint, headers=self.headers)
            print(request)
            print(dir(request))
            print(request.json())
        else:
            request = http_method(endpoint, headers=self.headers, json=body)
        return request.json()

    def get(self, path):
        return self.send_request(requests.get, path)

    def post(self, path, body=None):
        return self.send_request(requests.post, path, body)
