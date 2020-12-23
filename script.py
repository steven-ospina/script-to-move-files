import os
from sys import argv
import shutil

# Atributos
dictionary_files: dict = {}
size_numbers: list = []
flag_4: bool = False
flag_5: bool = True
number_folder: int = 0

# Filtra  y agrega los datos en una lista
os.chdir(argv[1])
cwd = os.getcwd()
list_files = os.listdir(cwd)
leaked_files = [value for value in list_files if ".xml" in value]

# Lista y reconoce el tamaño de los archivos y los agrega a un diccionario
# y el tamaño de los archivos los agrega a una lista
for value in leaked_files:
    size = os.stat(value)
    dictionary_files.update({size.st_size: value})
    size_numbers.append(size.st_size)

# Organiza los archivos de menor a mayor
size_numbers.sort()


# Función para obtener la longitud de las carpetas creadas
def get_size_folder(path_dir: str) -> int:
    list_files = os.listdir(path_dir)
    length = len(list_files)
    return length


# Función para crear las carpetas
def mkdir_folder(number: int) -> None:
    os.mkdir(str(number))


# Función para mover los archivos en las carpetas creadas
def move_file(value: int, number_folder: int) -> int:
    shutil.move(f"{cwd}/{dictionary_files[value]}", f"{cwd}/{str(number_folder)}/{dictionary_files[value]}")
    get = get_size_folder(f"{cwd}/{number_folder}/")
    print(f"  ►{dictionary_files[value]} Size Bytes ► {value}")
    return get


def print_number_folder(number_folder):
    print(f"{number_folder} ▼")


try:
    number_folder = number_folder + 1
    mkdir_folder(number=number_folder)
    print_number_folder(number_folder=number_folder)
    for value in size_numbers:
        if flag_5:
            get = move_file(value=value, number_folder=number_folder)
            if get >= 5:
                number_folder = number_folder + 1
                mkdir_folder(number=number_folder)
                print_number_folder(number_folder=number_folder)
                flag_5 = False
                flag_4 = True
                continue
        if flag_4:
            get2 = move_file(value=value, number_folder=number_folder)
            if get2 >= 4:
                number_folder = number_folder + 1
                mkdir_folder(number=number_folder)
                print_number_folder(number_folder=number_folder)
                continue

except Exception as error:
    print(error)
finally:
    print(f"Total xml ► ► {len(size_numbers)} ◄ ◄")
