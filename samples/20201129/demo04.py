import json

json_obj = {"access_token": "39_1pCqvkfQD4P33vqkY3cvJJM8KKQ9y5NRgC2pI0_jHTawE7kAQ3BzZ6daXizZco0bU-Rc-L3QX0H5mwM5n67jFDlN_AbwZsAMmRKc_deOSIsotlpDhm8Rcs5rQRVZfyRQWXZO6EFU3gspwxkSRBPeACAAKY"}

except_str = '{"expires_in":"7200"}'
except_dict = json.loads(except_str)

if list(except_dict.items()) in list(json_obj.items()):
    print(True)


yes_no = []

for except_item in list(except_dict.items()):
    if list(except_dict.items()) in list(json_obj.items()):
        yes_no.append(True)
    else:
        yes_no.append(False)
if False in yes_no:
    print(False)
else:
    print(True)