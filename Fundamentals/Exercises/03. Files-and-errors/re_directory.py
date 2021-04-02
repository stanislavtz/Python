import os, shutil

def make_dir(f):
    ext = f.split('.')[-1]
    dir_name = f"{ext}s"
    if not dir_name in os.listdir(output_path):
        os.mkdir(f"{output_path}/{dir_name}")
    
def replace_file(f):
    ext = f.split('.')[-1]
    dir_name = f"{ext}s"

    src = f"{input_path}/{f}"
    dst = f"{output_path}/{dir_name}/{f}"
    
    shutil.copy(src, dst)


path = './re_directory'
input_path = f'{path}/input'
output_path = f'{path}/output'

if not 'output' in os.listdir(path):
    os.mkdir(f"{path}/output")

root, dirs, files = next(os.walk(input_path))

[make_dir(file) for file in files]
[replace_file(file) for file in files]