from pathlib import Path

# Absolute path - we start from the root of the hard disk
# /usr/local/bin

# Relative path - from current directory to somewhere else
"""
path = Path("emails")  # if we dont pass anyhting it will refrence current directory
print(path.exists())
# print(path.mkdir())
print(path.rmdir())  # removes directory 
"""
path = Path()
for file in path.glob('*.*'):  # * - all files, *.py -python files
    print(file)
