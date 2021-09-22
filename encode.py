import json

src = 'C:<path>/json-encoder/data/creds.json'
dst = 'C:<path>/json-encoder/data/credsw.json'


with open(src, 'r') as reader:
    datas = json.load(reader)

creds = []
for data in datas['items']:
    logins = {}
    print(data)
    if data['login']:
        cred = data['login']
        username = cred['username']
        password = cred['password']
        logins['username'] = username
        logins['password'] = password
        if 'uris' in cred.keys():
            d = cred['uris'].pop()
            url = d['uri']
            logins['url'] = url
            creds.append(logins)

with open(dst, 'w') as json_file:
    json.dump(creds, json_file, indent=4)



