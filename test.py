client_key= 'CscQi7cWKghnWaQfLlqp5Jkdy'
client_secret='EMq1JHtJRKncXbavd9PbGo6ZF4OJHpsrg4YUaQvPxqhwubkJa6'

import base64
import requests

key_secret = '{}:{}'.format(client_key,client_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
access_token = auth_resp.json()['access_token']
search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)    
}

search_params = {
    'q': 'General Election',
    'result_type': 'recent',
    'count': 2
}

search_url = '{}1.1/search/tweets.json'.format(base_url)

search_resp = requests.get(search_url, headers=search_headers, params=search_params)

print(auth_resp.status_code)