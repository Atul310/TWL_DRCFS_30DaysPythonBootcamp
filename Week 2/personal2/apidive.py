#to get random api from interenet 
import requests
resp = requests.get("https://my-json-server.typicode.com/")
print(resp.json()) #we use ctrl shift + p  