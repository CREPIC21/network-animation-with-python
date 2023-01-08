import requests

r = requests.get('https://jsonplaceholder.typicode.com/todos').json()
# r.text
print(type(r))
print(r[2])
for element in r:
    if element['completed']:
        print(element)