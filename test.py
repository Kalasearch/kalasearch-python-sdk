# -*- coding: utf-8 -*-

from kalasearch import Client
import json

myclient = Client("YOUR_APP_ID", "YOUR_API_KEY")


index = myclient.get_index("YOUR_INDEX_ID")


documents = [
    {"name": "周杰伦"},
    {"name": "陈冠希"}
]

print(index.add_objects(documents))

options = {
    "searchableFields": ["name", "story"],
    "highlightFields": ["name", "story"]
}

search_results = index.search("冠希")
print(search_results)