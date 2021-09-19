import json

with open('C:/Users/markc_gphih48/Documents/development/python/json-encoder/data/creds.json','r') as reader:
    # for line in reader:
    #     if line.find('username') >= 0:
    #         print(line)
    #         print(len(line))
    datas = json.load(reader)

# with open('C:/Users/markc_gphih48/Documents/development/python/json-encoder/data/credsw.json','w') as json_file:
#     json.dump(data, json_file, indent=4)

for data in datas['items']:
    if data['login']:
        print(data['login'])
