# WRITING TO TEXT FILES

# w -> writes to the file but also overwtites everything else in the file if file already exists
with open('myfile.txt', 'w') as f:
    f.write('Second line.\n')
    f.write('Third line.\n')

# a -> appends to the file
with open('myfile.txt', 'a') as f:
    f.write('Forth line.\n')
    f.write('Fifth line.\n')

# r+ -> adds to the first line into existing file
with open('myfile.txt', 'r+') as f:
    f.write('Line added with r+.\n')

