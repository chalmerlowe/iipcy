# coding: utf-8
import requests as rq
import json

output = rq.request('get', 'http://iipcy.ws')

data = json.loads(str(output.content.decode('utf-8')))
print(data)
print(type(data))
for key, value in data.items():
    print(key.ljust(25), value)
