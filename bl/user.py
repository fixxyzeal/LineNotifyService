import requests
from requests.sessions import default_headers
import os
from dotenv import load_dotenv

load_dotenv()
url = os.environ.get('DATAAPIURL')+'/user'

def Authenticate(user, password):
    res = requests.post(url, json={'UserName': user, 'PassWord': password})
    data = res.json()
    print(data)
    return data
