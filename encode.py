import json

with open('C:/Users/markc_gphih48/Documents/development/python/json-encoder/data/creds.json','r') as reader:
    # for line in reader:
    #     if line.find('username') >= 0:
    #         print(line)
    #         print(len(line))
    datas = json.load(reader)
count = 1
creds = []
for data in datas['items']:
    logins = {}
    print(data)
    if data['login']:
        print(count)
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

with open('C:/Users/markc_gphih48/Documents/development/python/json-encoder/data/credsw.json','w') as json_file:
    json.dump(creds, json_file, indent=4)



