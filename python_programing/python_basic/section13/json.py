# JSON

import json

j = {
  "employee":
    [
      {"id": 111, "name": "Mike"},
      {"id": 222, "name": "Nancy"}
    ]
}

print(j)
print("#############")
# dictionaryの形をdumpsでJSONにしてやる
print(json.dumps(j))

with open('test.json', 'w') as f:
    json.dump(j, f)

print("#############")

with open('test.json', 'r') as f:
    json.dump(f)

