

with open('C:/Users/markc_gphih48/Documents/development/python/json-encoder/data/creds.json','r') as reader:
    for line in reader:
        if line.find('username') >= 0:
            print(line)
            print(len(line))



