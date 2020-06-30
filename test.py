from kalasearch import Client

myclient = Client("3bc797e5-9538-4374-a82c-36a4cd9c0071", "19f9453a-8b9d-4af3-8021-d40fcd0f0dc2")


index = myclient.get_index("bc4099ed-32bd-4262-9333-1b05398913fd")


document = {'name': 'Jay', 'published':'abc'}

print(index.add_document(document))

print(index.search("jay"))