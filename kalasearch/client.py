from .index import Index
from .config import Config

class Client():
    """
    KalaSearch's Python client.

    """
    config = None

    def __init__(self, appId, apiKey):
        self.config = Config(appId, apiKey)
    
    def get_index(self, index_id):
        return Index(self.config, index_id)
        