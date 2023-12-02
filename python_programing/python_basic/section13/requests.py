# requests

# urllibより簡単に操作できるthirdpartyのライブラリ

import requests


payload = {'key1': 'value1', 'key2': 'value2'}

# GET
r = requests.get('http://httpbin.org/get', params=payload)

# POST
r = requests.post('http://httpbin.org/post', data=payload)

# PUT
r = requests.put('http://httpbin.org/put', data=payload)

# DELETE
r = requests.delete('http://httpbin.org/delete', data=payload)

# timeoutも設定できる
r = requests.get('http://httpbin.org/get', params=payload, timeout=0.01)

print(r.status_code)
print(r.text)
print(r.json())
