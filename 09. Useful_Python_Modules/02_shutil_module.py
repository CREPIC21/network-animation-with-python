import shutil # https://docs.python.org/3/library/shutil.html

# Copy the contents (no metadata) of the file named src to a file named dst and return dst in the most efficient way possible
shutil.copyfile('./dir_01/dir_01.txt', './dir_02/dir_02_copy01.txt')

# Copies the file src to the file or directory dst. src and dst should be path-like objects or strings
shutil.copy('./dir_01/dir_01.txt', './dir_02')

# Identical to copy() except that copy2() also attempts to preserve file metadata
shutil.copy2('./dir_01/dir_01.txt', './dir_02/dir_02_copy02.txt')

# Recursively copy an entire directory tree rooted at src to a directory named dst and return the destination directory
shutil.copytree('./dir_02', './dir_01/dir_01_copy_to')

# Recursively move a file or directory (src) to another location (dst) and return the destination
shutil.move('./dir_01', './dir_01_new_name')

# Delete an entire directory tree; path must point to a directory (but not a symbolic link to a directory)
shutil.rmtree('./dir_03')