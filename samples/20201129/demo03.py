import json

str1 = '{"access_token": "39_1pCqvkfQD4P33vqkY3cvJJM8KKQ9y5NRgC2pI0_jHTawE7kAQ3BzZ6daXizZco0bU-Rc-L3QX0H5mwM5n67jFDlN_AbwZsAMmRKc_deOSIsotlpDhm8Rcs5rQRVZfyRQWXZO6EFU3gspwxkSRBPeACAAKY"}'

json_obj = json.loads(str1)

if 'access_token' in json_obj.keys():
    print('True')
else:
    print('Flase')


check_keys = ['access_token','expires_in']
yes_no = []
for check_key in check_keys:
    if check_key in json_obj.keys():
        yes_no.append(True)
    else:
        yes_no.append(False)
if False in yes_no:
    print(False)