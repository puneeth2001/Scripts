import wunderpy2,webbrowser
import requests, json
import urllib.request
with open('wunderlist-credentials.json') as data_file:
    oauth = json.load(data_file)

uri = oauth['authentication_url'] % (oauth['client_id'], oauth['callback_url'])
res = urllib.request.urlopen(uri)
finalurl = res.geturl()
print(finalurl)
'''r = requests.get(uri)
r.url
'''
def root():
    uri = oauth['authentication_url'] % (oauth['client_id'], oauth['callback_url'])
    return redirect(uri)


def callback():
    code = request.args.get('code')
    uri = oauth['token_url']
    params = {'client_id': oauth['client_id'], 'client_secret': oauth['client_secret'], 'code': code, 'grant_type': 'authorization_code', 'redirect_uri': oauth['callback_url']}
    resp = requests.get(uri, params)
    r = json.loads(resp.read())
    oauth['token'] = r['access_token']


