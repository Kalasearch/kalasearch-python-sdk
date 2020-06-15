from kalasearch import Client

myclient = Client("30bd6466-b03b-4289-baa8-cd745c5b9c33", "5d47ad94-0cd8-4d15-b4a1-283e932e6d1e")


index = myclient.get_index("5a84eb90-ec74-47d2-acb6-8fb6f6fc0878")


document = {'name': 'Jay', 'published':'abc'}

print(index.add_document(document))

