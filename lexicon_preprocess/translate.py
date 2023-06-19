import requests, uuid
from googletrans import Translator
import os
 
class BingTranslator:
    def __init__(self) -> None:
        key = os.getenv("MICROSOFT_TRANSLATE_KEY")
        endpoint = "https://api.cognitive.microsofttranslator.com"
        location = "westeurope"
        path = '/translate'
        self.constructed_url = endpoint + path
        self.params = {
            'api-version': '3.0',
            'from': 'en',
            'to': ['hr']
        }
        self.headers = {
            'Ocp-Apim-Subscription-Key': key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }
        self.ctr = 0

    def translate(self, word):
        translations = []

        body = [{
            'text': word
        }]

        request = requests.post(self.constructed_url, params=self.params, headers=self.headers, json=body)
        response = request.json()
        translations.append(response[0]["translations"][0]["text"])

        self.ctr += 1
        print(self.ctr)
        return translations

  
class GoogleTranslator:
    def __init__(self) -> None:
        self.translator = Translator()
        self.ctr = 0

    def translate(self, word):
        text = ""
        while text == "":
            try:
                parsed = self.translator.translate(word, dest="hr", src="en")
                text = parsed.text
            except Exception:
                print("exception for " + word)
    
        return text