import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

URL = "https://api.api-ninjas.com/v1/quotes"
headers = {"X-Api-Key": api_key}

# def get_quote():
#     response = requests.get(URL, headers=headers)
#     data = response.json()
#     return data

# def load_quote():
#     while True:
#         data = get_quote()
#         if len(data[0]["quote"]) < 120:    
#             break
#     return {
#         "quote": data[0]["quote"],
#         "author": data[0]["author"],
#         "quote length": len(data[0]["quote"])
#     }

def get_quote():
    response = requests.get(URL, headers=headers)
    data = response.json()
    return {
        "quote": data[0]["quote"],
        "author": data[0]["author"],
    }
        