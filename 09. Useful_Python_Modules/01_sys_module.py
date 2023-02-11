### IMPORTANT ###
"""
Run the script from the cmd or terminal, so you can pass argumenst
- example: python .\01_sys_module.py python java go
"""

import sys # https://docs.python.org/3/library/sys.html

# print(f'Number of arguments: {len(sys.argv)}')
# print(f'This is the name of the script: {sys.argv[0]}')
# print(f'The script arguments are: {sys.argv}')
# print(f'The script arguments are: {sys.argv[1:]}')

if len(sys.argv) >= 2:
    for item in sys.argv[1:]:
        with open(item, 'r') as f:
            print(f.read())
else:
    print('Wrong number of arguments. The script needs to be executed with at least one argument.')

# - example: python .\01_sys_module.py .\test_01.txt .\test_02.txt