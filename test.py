# -*- coding: utf-8 -*-

from kalasearch import Client
import json

myclient = Client("592918d4-32b0-4fb6-8000-4d8a3781251f", "f623e196-1dd4-4f89-8421-9354d2a6cfec")


index = myclient.get_index("72cda695-1a48-4a3e-8b80-0ccb36d408b1")


documents = [
    {"name": "大话西游1"},
    {"name": "大话西游2"},
    {"name": "大话西游3"},
    {"name": "大话西游4"}
]

#print(index.add_document(document))
index.add_documents(documents)


options = {
    "searchableFields": ["name", "story"],
    "highlightFields": ["name", "story"]
}

search_results = index.search("chen")
print(search_results)
