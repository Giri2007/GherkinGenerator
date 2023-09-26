import requests
import json


class openAiConnect:

    @staticmethod
    def readData():
        with open('secretData.json', 'r') as json_file:
            data = json.load(json_file)
            access_token = data['API_key']
        return access_token

    def call_api(self, prompt, api_key, engine="text-davinci-002", max_tokens= 500):
        while True:
            url = "https://api.openai.com/v1/engines/{}/completions".format(engine)
            headers = {
                "Authorization": "Bearer " + api_key,
                "Content-Type": "application/json"
            }
            data = {
                "prompt": "generate multiple gherkin syntax for" + prompt,
                "max_tokens": max_tokens
            }

            response = requests.post(url, headers=headers, json=data)

            if response.status_code == 200:
                return response.json()
            else:
                print("Error:", response.status_code)
                print(response.text)
                return None

