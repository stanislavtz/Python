import os
import shutil


def make_dir_from_file_extention(f):
    ext = f.split('.')[-1]
    dir_name = f"{ext}s"
    path = output_path

    create_dir(dir_name, path)

def replace_file(f):
    ext = f.split('.')[-1]
    dir_name = f"{ext}s"

    src = f"{input_path}/{f}"
    dst = f"{output_path}/{dir_name}/{f}"

    shutil.copy(src, dst)

def create_dir(dir_name, path):
    if not dir_name in os.listdir(path):
        os.mkdir(f"{path}/{dir_name}")

def rename_file(f, v, n_v):
    if v in f:
        src = f"{input_path}/{f}"
        n_f = f.replace(v, n_v)
        dst = f"{renamed_path}/{n_f}"

        shutil.copy(src, dst)


path = './re_directory'
input_path = f'{path}/input'
output_path = f'{path}/output'
renamed_path = f'{path}/renamed'

root, dirs, files = next(os.walk(input_path))

create_dir('output', path)
create_dir('renamed', path)
[make_dir_from_file_extention(file) for file in files]
[replace_file(file) for file in files]

value_to_rename = input()
new_value = input()
[rename_file(file, value_to_rename, new_value) for file in files]