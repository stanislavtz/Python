import os
size = 0

root, dirs, files  = next(os.walk('./products', topdown=True))
    # if len(files) == 0:
    #     break
for f in files:
    size += os.stat('./products/'+f).st_size

with open('./folder_size/output.txt', 'w') as output_file:
    output_file.write(str(size/1024/1024)+'\n')