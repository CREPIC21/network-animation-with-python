import json
# https://pynative.com/python-json-load-and-loads-to-parse-json/#:~:text=load()%20is%20used%20to,that%20contains%20a%20JSON%20document.

with open('friends.json', 'rt') as f:
    obj = json.load(f)
    print(type(obj))
    print(obj)

json_string = """{
    "Dan": [
        20,
        "London",
        3234543
    ],
    "Maria": [
        25,
        "Madrid",
        43562543
    ]
}"""
obj = json.loads(json_string)
print(type(obj))
print(obj)
