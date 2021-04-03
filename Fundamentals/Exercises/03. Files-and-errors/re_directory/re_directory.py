import os
import shutil


def make_dir_from_file_extention(file, path):
    ext = file.split('.')[-1]
    dir_name = f"{ext}s"

    create_dir(dir_name, path)

def replace_file(file, input_path, output_path):
    ext = file.split('.')[-1]
    dir_name = f"{ext}s"

    src = f"{input_path}/{file}"
    dst = f"{output_path}/{dir_name}/{file}"

    shutil.copy(src, dst)

def create_dir(dir_name, path):
    if not dir_name in os.listdir(path):
        os.mkdir(f"{path}/{dir_name}")

def rename_file(file, input_path, renamed_path, value_to_rename, new_value):
    if value_to_rename in file:
        src = f"{input_path}/{file}"
        new_file = file.replace(value_to_rename, new_value)
        dst = f"{renamed_path}/{new_file}"

        shutil.copy(src, dst)


path = './re_directory'
input_path = f'{path}/input'
output_path = f'{path}/output'
renamed_path = f'{path}/renamed'

root, dirs, files = next(os.walk(input_path))

create_dir('output', path)
create_dir('renamed', path)
[make_dir_from_file_extention(file, output_path) for file in files]
[replace_file(file, input_path, output_path) for file in files]

value_to_rename = input()
new_value = input()
[rename_file(file, input_path, renamed_path, value_to_rename, new_value) for file in files]