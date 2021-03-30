import os
path = './file_extentions/input'

inp = input()

for root, dirs, files in os.walk(path):
    for f in files:
        if f.split('.')[-1] == inp:
            print(f)