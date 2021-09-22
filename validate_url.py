import requests
import json

src = 'C:<path>/json-encoder/data/credsw.json'
valid_dst = 'C:<path>/json-encoder/data/credsvalid.json'
invalid_dst = 'C:<path>/json-encoder/data/credserror.json'


with open(src, 'r') as reader:
    datas = json.load(reader)

validated = []
timedout = []
for data in datas:
    print(data)
    url = data['url']
    try:
        response = requests.get(url, timeout=5)#might try a time out situation
    except Exception:
        timedout.append(data)

    if response:
        validated.append(data)
    else:
        timedout.append(data)


with open(valid_dst, 'w') as json_file:
    json.dump(validated, json_file, indent=4)

with open(invalid_dst, 'w') as json_file:
    json.dump(timedout, json_file, indent=4)


