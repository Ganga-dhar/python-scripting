import os

path = "mathyam"

if os.path.isfile(path):
    print(f"{path} is a file")
elif os.path.isdir(path):
    print(f"{path} is a directory")
else:
    print("Not found")
if os.path.exists(path):
    print(f"{path} exists")
else:
    print(f"{path} does not exist")