import os
size = 0

for root, dirs, files in os.walk('.', topdown=True):
    if len(files) == 0:
        break
    for f in files:
        size += os.stat(f).st_size

with open('./folder_size/output.txt', 'w') as output_file:
    output_file.write(str(size/1024/1024)+'\n')
