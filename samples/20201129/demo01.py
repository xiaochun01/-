import requests
import re
session = requests.session()

get_param_dict={
    "grant_type":"client_credential",
    "appid":"wx55614004f367f8ca",
    "secret":"65515b46dd758dfdb09420bb7db2c67f"
}

response = session.get( url='https://api.weixin.qq.com/cgi-bin/token',
                         params=get_param_dict)
print( response.content.decode('utf-8') )

token = re.findall('"access_token":"(.+?)"',response.text)[0]
print(token)