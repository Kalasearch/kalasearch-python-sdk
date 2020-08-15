# -*- coding: utf-8 -*-

from kalasearch import Client
import json

myclient = Client("", "")


index = myclient.get_index("")


documents = [
    {"name": "陈冠希1"},
    {"name": "陈冠希2"}
]

#print(index.add_document(document))
print(index.add_objects(documents))



options = {
    "searchableFields": ["name", "story"],
    "highlightFields": ["name", "story"]
}

search_results = index.search("冠希")
print(search_results)
