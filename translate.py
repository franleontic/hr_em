import requests, uuid, json
from googletrans import Translator

class BingTranslator:
    def __init__(self) -> None:
        key = "c0bfc1e5aee740a3a47d980c34b09410"
        endpoint = "https://api.cognitive.microsofttranslator.com"
        location = "westeurope"
        path = '/dictionary/lookup'
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
        print(response)
        for resp in response[0]["translations"]:
            if resp["confidence"] > 0.2:
                translations.append(resp["normalizedTarget"])

        self.ctr += 1
        print(self.ctr)
        return translations
    
      
class BingTranslator_Single:
    def __init__(self) -> None:
        key = "c0bfc1e5aee740a3a47d980c34b09410"
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
        translations = set()
        try:
            parsed = self.translator.translate(word, dest="hr", src="en").extra_data["parsed"]
            tr_orig1 = parsed[1][0][0][-1][-1][0]
            tr_orig2 = parsed[1][0][0][-1][-1][-1][-1][0]
            translations.add(tr_orig1)
            translations.add(tr_orig2)
            tr = parsed[-1][-5]
            if tr != None:
                all_translations = tr[0][0][1]
                for tr in all_translations:
                    translations.add(tr[0])
            self.ctr += 1
            print(self.ctr)
        except Exception:
            print("exception for " + word)
 
        return translations