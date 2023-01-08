#OPENING AND READING FILES

# rt -> text mode
# rb -> binary mode
f = open('configuration.txt', 'rt')
content = f.read()
print(content)
print(f.closed)
f.close()

print(f.closed)
f = open('configuration.txt', 'rt')
line = f.readline()
print(line)
f.close()

print('#' * 50)
# using with the file will be closed automatically
with open('configuration.txt', 'rt') as f:
    content = f.read()
    print(content)
print(f.closed)
