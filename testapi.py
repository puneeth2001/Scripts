import wunderpy2,webbrowser
import requests, json

with open('wunderlist-credentials.json') as data_file:
    oauth = json.load(data_file)

uri = oauth['authentication_url'] % (oauth['client_id'], oauth['callback_url'])
r = requests.get(uri)
webbrowser.open(r.url)
print(r.url)



