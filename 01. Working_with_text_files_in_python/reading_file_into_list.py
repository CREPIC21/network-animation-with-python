# READING FILES INTO A LIST

# 1. f.read().splitlines()
with open('configuration.txt') as f:
    content = f.read().splitlines()
    print(content)
print('1.#' * 50)

# 2. f.readlines()
with open('configuration.txt') as f:
    content = f.readlines()
    print(content)
print('2.#' * 50)

# 3. f.readline() -> reads line by line
with open('configuration.txt') as f:
    content = f.readline()
    print(content, end='')
    content = f.readline()
    print(content)
    content = f.readline()
    print(content)
print('3.#' * 50)

# 4. list(f)
with open('configuration.txt') as f:
    content = list(f)
    print(content)
print('4.#' * 50)

# iterate over the file
with open('configuration.txt') as f:
    for line in f:
        print(line, end='')
print('5.#' * 50)