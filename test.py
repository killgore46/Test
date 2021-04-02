import requests
import os

r = requests.get('https://google.com')
print(r.status_code)
