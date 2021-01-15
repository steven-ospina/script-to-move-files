import os
from sys import argv
import shutil

# Atributos
dictionary_files: dict = {}
size_numbers: list = []
flag_4: bool = False
flag_5: bool = True
number_folder: int = 0
color_green_console: str = '\33[32m'
color_blue_console: str = '\33[34m'
color_yellow_console: str = '\33[33m'
color_red_console: str = '\033[91m'
color_end_console: str = '\033[0m'
text_bold_console: str = '\33[1m'

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
    print(f"  ►{print_blue(text=dictionary_files[value])} {print_green(text='Size Bytes')} ► {print_yellow(text=value)}")
    return get


def print_number_folder(number_folder) -> None:
    print(f"{print_yellow(text=str(number_folder))} {print_yellow(text='▼')}")


def print_blue(text: str) -> str:
    return f"{color_blue_console}{text_bold_console}{text}{color_end_console}"


def print_yellow(text: str) -> str:
    return f"{color_yellow_console}{text_bold_console}{text}{color_end_console}"


def print_green(text: str) -> str:
    return f"{color_green_console}{text_bold_console}{text}{color_end_console}"


def print_red(text: str, message_Exception: Exception) -> str:
    message_form = f"{color_red_console}{text_bold_console}{text}:{message_Exception}{color_end_console}"
    return message_form


try:
    number_folder = number_folder + 1
    mkdir_folder(number=number_folder)
    print_number_folder(number_folder=number_folder)
    for number_value in size_numbers:
        if flag_5:
            size_folder = move_file(value=number_value, number_folder=number_folder)
            first_folder = 5
            if size_folder >= first_folder:
                number_folder = number_folder + 1
                mkdir_folder(number=number_folder)
                print_number_folder(number_folder=number_folder)
                flag_5 = False
                flag_4 = True
                continue
        if flag_4:
            size_folder2 = move_file(value=number_value, number_folder=number_folder)
            other_folders = 4
            if size_folder2 >= other_folders:
                number_folder = number_folder + 1
                mkdir_folder(number=number_folder)
                print_number_folder(number_folder=number_folder)
                continue
    # Chequea para verificar si una carpeta que sin archivos y la elimina
    size_end_folder = get_size_folder(f"{cwd}/{number_folder}/")
    if size_end_folder == 0:
        os.rmdir(f"{cwd}/{number_folder}/")
        print(print_green(f'Se elimino la carpeta "{str(number_folder)}" por que esta vaciá'))
    print(f" {print_green(text='Total xml')} ► ► {len(size_numbers)} ◄ ◄")
except Exception as error:
    print(print_red(text="ERROR", message_Exception=error))
