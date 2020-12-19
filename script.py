import os
from sys import argv
import shutil

list_dir = []
size_files = {}
size_number = []
flag_4 = False
flag_5 = True
number_folder = 0

os.chdir(argv[1])
cwd = os.getcwd()
list_files = os.listdir(cwd)
list_dir = [value for value in list_files if ".xml" in value]

for value in list_dir:
    size = os.stat(value)
    size_files.update({size.st_size: value})
    size_number.append(size.st_size)

size_number.sort()


def get_size_folder(list_dir):
    list_files = os.listdir(list_dir)
    length = len(list_files)
    return length


def mkdir_folder(number):
    os.mkdir(str(number))


try:
    number_folder = number_folder + 1
    mkdir_folder(number_folder)
    print(number_folder)
    for value in size_number:
        if flag_5:
            shutil.move(f"{cwd}/{size_files[value]}", f"{cwd}/{str(number_folder)}/{size_files[value]}")
            get = get_size_folder(f"{cwd}/{number_folder}/")
            print(f"{size_files[value]}")
            if get >= 5:
                flag_5 = False
                flag_4 = True
                number_folder = number_folder + 1
                mkdir_folder(number_folder)
                print(number_folder)
                continue
        if flag_4:
            shutil.move(f"{cwd}/{size_files[value]}", f"{cwd}/{str(number_folder)}/{size_files[value]}")
            get2 = get_size_folder(f"{cwd}/{number_folder}/")
            print(f"{size_files[value]}")
            if get2 >= 4:
                number_folder = number_folder + 1
                mkdir_folder(number_folder)
                print(number_folder)
                continue

except Exception as error:
    print(error)
