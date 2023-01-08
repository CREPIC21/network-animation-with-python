import json
# https://pynative.com/python-json-dumps-and-dump-for-json-encoding/#:~:text=dump()%20method%20(without%20%E2%80%9Cs,object%20into%20JSON%20formatted%20String.

friends = {'Dan': [20, 'London', 3234543], 'Maria': [25, 'Madrid', 43562543]}

with open('friends.json', 'w') as f:
    json.dump(friends, f, indent=4)

json_string = json.dumps(friends, indent=4)
print(json_string)