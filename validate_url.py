import requests
import json

src = fr'C:<>.json'
valid_dst = fr'C:<>.json'
invalid_dst = fr'C:<>.json'


with open(src, 'r') as reader:
    datas = json.load(reader)

validated = []
timedout = []
for data in datas:
    print(data)
    url = data['url']
    try:
        response = requests.get(url, timeout=5)#might try a time out situation
        if response.ok: #todo this needs to be redesigned
            validated.append(data)
        else:
            timedout.append(data)
    except Exception:
        timedout.append(data)




with open(valid_dst, 'w') as json_file:
    json.dump(validated, json_file, indent=4)

with open(invalid_dst, 'w') as json_file:
    json.dump(timedout, json_file, indent=4)


