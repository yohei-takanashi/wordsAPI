from dotenv import load_dotenv
import os
import requests


load_dotenv()
api_key = os.environ.get("API_KEY")
word = "example"
definition_url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/definitions"
synonyms_url = f"http://wordsapiv1.p.rapidapi.com/words/{word}/synonyms"

definition_response = requests.get(definition_url)
synonyms_response = requests.get(synonyms_url)
