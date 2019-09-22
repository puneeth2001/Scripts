import requests
import json
import wunderpy2
import urllib
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

with open('wunderlist-credentials.json') as data_file:
    oauth = json.load(data_file)

code = ""
ACCESS_TOKEN_URL = 'https://www.wunderlist.com/oauth/access_token'

def get_access_token(code, client_id, client_secret):
        headers = {
                'Content-Type' : 'application/json'
                }
        data = {
                'client_id' : client_id,
                'client_secret' : client_secret,
                'code' : code,
                }
        str_data = json.dumps(data)
        response = requests.request(method='POST', url=ACCESS_TOKEN_URL, headers=headers, data=str_data)
        body = response.json()
        status_code = response.status_code
        if status_code != 200:
            raise ValueError("{} -- {}".format(status_code, response.json()))
        return body['access_token']

@app.route('/')
def root():
    uri = oauth['authentication_url'] % (oauth['client_id'], oauth['callback_url'])
    return redirect(uri)

@app.route('/callback/wunderlist', methods=["GET"])
def callback():
    code = request.args.get('code')
    access_token = get_access_token(code, '12cdd0bb0de5cdfd1208', 'bee3e57899fcd7ffaf48c64ed21fe9935e10493e3c0d11e9ef27c74d4770')   
    client_id = '12cdd0bb0de5cdfd1208'
    list_id = '403671590'
    headers={'X-Access-Token': access_token, 'X-Client-ID': client_id, 'Content-Type' : 'application/json'}
    f = requests.get('https://a.wunderlist.com/api/v1/tasks', headers=headers,params = {'list_id':list_id,'completed':True})
    j = json.loads(f.text)

    sobject = slice(8,10)
    for i in j:
        if(i['completed_at'][sobject]>'20'):
            print(i['title'])    
    return "Ok"



if __name__ == "__main__":
    app.secret_key = '53421'
    app.run(debug=True)
    print(code)
