# ABSOLUTE AND RELATIVE PATHS

### WINDOWS ###
# error
# f = open('C:\Users\crepi\PycharmProjects\Network_Automation_With_Python\01. Working_with_text_files_in_python\configuration.txt')

# no error -> by adding 'r' before the string
# f = open(r'C:\Users\crepi\PycharmProjects\Network_Automation_With_Python\01. Working_with_text_files_in_python\configuration.txt')

# no error -> by using double forward slashes
f = open('C:\\Users\\crepi\\PycharmProjects\\Network_Automation_With_Python\\01. Working_with_text_files_in_python\\configuration.txt')

### relative path
# . -> current working directory
# .. -> parent directory