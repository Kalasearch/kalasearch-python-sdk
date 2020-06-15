
class Config():
    appId = None
    apiKey = None
    domain = "https://api.kalasearch.cn"

    def __init__(self, appId, apiKey):
        self.appId = appId
        self.apiKey = apiKey