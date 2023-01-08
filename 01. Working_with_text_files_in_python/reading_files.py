f = open('configuration.txt', 'rt')
# read only first 5 characters
content = f.read(5)
print(content)

# reading the next 3 characters
content = f.read(3)
print(content)

# gives the position of the cursor in the file
print(f.tell())

# moving the cursor in the file on position 2
f.seek(2)
content = f.read(3)
print(content)

# moving the cursor in the file on position 0
f.seek(0)
content = f.read(3)
print(content)