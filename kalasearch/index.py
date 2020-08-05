from .http_client import HttpClient

class Index():
    config = None
    index_id = ""
    http_client = None

    def __init__(self, config, index_id):
        self.config = config
        self.index_id = index_id
        self.http_client = HttpClient(self.config)

    def get_info(self):
        path = 'indexes/{}/info'.format(self.index_id)
        return self.http_client.get(path)
    
    def add_document(self, document):
        path = 'indexes/{}/docs'.format(self.index_id)
        return self.http_client.post(path, document)

    def add_documents(self, documents):
        path = 'indexes/{}/docs/batch'.format(self.index_id)
        return self.http_client.post(path, documents)
    
    def search(self, query, options=None):
        if options is None:
            options = {}
        path = 'indexes/{}/query'.format(self.index_id)
        search_params = {
            'query': query,
            **options
        }
        return self.http_client.post(path, search_params)