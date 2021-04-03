import os

path = './input'
f_extension = input()
root, dirs, files = next(os.walk(path))
[print(f) for f in files if f.split('.')[-1] == f_extension]