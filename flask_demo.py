
import urllib
import json
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# set the callback url
# and get the client_id and client_secret at
# https://developer.wunderlist.com/applications
#
# doc for WL API
# https://developer.wunderlist.com/documentation

# add 'mysite/' before filename below if deploying on Pythonanywhere
with open('wunderlist-credentials.json') as data_file:
    oauth = json.load(data_file)

@app.route('/')
def root():
    uri = oauth['authentication_url'] % (oauth['client_id'], oauth['callback_url'])
    return redirect(uri)

@app.route('/callback/wunderlist', methods=["GET"])
def callback():
    code = request.args.get('code')
    return True


if __name__ == "__main__":
    app.secret_key = '53421'
    app.run(debug=True)