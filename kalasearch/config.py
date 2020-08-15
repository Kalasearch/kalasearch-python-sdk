
class Config():
    appId = None
    apiKey = None
    domain = None

    def __init__(self, appId, apiKey, domain):
        self.appId = appId
        self.apiKey = apiKey
        self.domain = domain