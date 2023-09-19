import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response_body = requests.get(self.url)
        return response_body.content

    def load_json(self):
        response_list =[]
        responses = json.loads(self.get_response_body())
        for response in responses:
            response_list.append(response)

        return response_list
    
example = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
toprint1 = example.get_response_body()
print(toprint1)

toprint2 = example.load_json()
print(toprint2)
