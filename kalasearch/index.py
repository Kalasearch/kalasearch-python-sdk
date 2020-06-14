import requests

class Index():
    api_domain = "https://api.kalasearch.cn"
    config = None
    index_id = ""

    def __init__(self, config, index_id):
        self.config = config
        self.index_id = index_id
    
    @staticmethod
    def get_index(config, index_id):
        return Index(config, index_id)