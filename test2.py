import wunderpy2

api = wunderpy2.WunderApi()
access_token = api.get_access_token('87a4c2ebad6f82374d77', '12cdd0bb0de5cdfd1208', 'bee3e57899fcd7ffaf48c64ed21fe9935e10493e3c0d11e9ef27c74d4770')   # Fill in your values here
client = api.get_client(access_token, '12cdd0bb0de5cdfd1208') 
print(client.get_lists())