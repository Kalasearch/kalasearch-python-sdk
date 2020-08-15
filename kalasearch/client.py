from .index import Index
from .config import Config

class Client():
    """
    KalaSearch's Python client.

    """
    config = None

    def __init__(self, appId, apiKey, domain="https://api.kalasearch.cn/v1"):
        self.config = Config(appId, apiKey, domain)
    
    def get_index(self, index_id):
        return Index(self.config, index_id)
        