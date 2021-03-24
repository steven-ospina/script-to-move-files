import os
from sys import argv
import shutil
import sys

# Atributos
color_green_console: str = '\33[32m'
color_blue_console: str = '\33[34m'
color_yellow_console: str = '\33[33m'
color_red_console: str = '\033[91m'
color_end_console: str = '\033[0m'
text_bold_console: str = '\33[1m'


def print_blue(text: str) -> str:
    """ Función para imprimir en la terminal con color azul.

    Args:
        text (str): Recibe el texto que se va a convertir en color azul.

    Returns:
        str: Retorna el texto en color azul.
    """
    return f"{color_blue_console}{text_bold_console}{text}{color_end_console}"


def print_yellow(text: str) -> str:
    """ Función para imprimir en la terminal con color amarillo.

    Args:
        text (str): Recibe el texto que se va a convertir en color amarillo.

    Returns:
        str: Retorna el texto en color amarillo.
    """
    return f"{color_yellow_console}{text_bold_console}{text}{color_end_console}"


def print_green(text: str) -> str:
    """ Función para imprimir en la terminal con color verde.

    Args:
        text (str): Recibe el texto que se va a convertir en color verde.

    Returns:
        str: Retorna el texto en color verde.
    """
    return f"{color_green_console}{text_bold_console}{text}{color_end_console}"


def print_red(text: str, message_Exception: Exception) -> str:
    """ Función para imprimir en la terminal con color rojo.

    Args:
        text (str): Recibe el texto que se va a convertir en color rojo.
        message_Exception (Exception): Recibe el mensaje de error.

    Returns:
        str: Retorna el texto en color rojo.
    """
    message_form = f"{color_red_console}{text_bold_console}{text}:{message_Exception}{color_end_console}"
    return message_form


def organize_data(list_data: list):
    """ Función para organizar los archivos XML.

    Args:
        text (str): Recibe una lista con los nombres de los archivos XML.

    Returns:
        str: Retorna un diccionario con los datos organizados por:
        {key = Número de la carpeta : value = Lista con los archivos XML }
    """
    try:
        length_list = len(list_data)
        if length_list <= 0:
            print(print_yellow(text="No hay archivos XML en el directorio o ya están organizados."))
            sys.exit()
        start = 0
        first_folder = 5
        other_folders = 4
        folder = first_folder
        folder_counter = 0
        root_dictionary = {}
        while True:
            folder_counter += 1
            formula = start + folder
            split_list = list_data[start:formula]
            if formula <= length_list:
                root_dictionary.update({folder_counter: split_list})
            else:
                end_length = len(split_list)
                if end_length >= 1:
                    root_dictionary.update({folder_counter: split_list})
                break
            if folder == first_folder:
                folder = other_folders
            start = formula
        return root_dictionary
    except Exception as error_in_organize_data:
        print(print_red(text="Error al organizar los archivos XML", message_Exception=error_in_organize_data))


def get_files_and_path(path: str) -> tuple:
    """ Función para obtener la lista de los archivos en el directorio,
        que le indiquen y filtrar por archivos XML.

    Args:
        path (str): Recibe la ruta absoluta del directorio en donde están,
        los archivos.

    Returns:
        tuple: Retorna la lista con los archivos XML y la ruta completa en donde,
        están los archivos.
    """
    os.chdir(path)
    cwd = os.getcwd()
    list_files = os.listdir(cwd)
    leaked_files = [value for value in list_files if ".xml" in value]
    return leaked_files, cwd


def sort_data(data_list: list) -> list:
    """ Función para organizar los archivos XML en orden ascendente con base,
        en el tamaño del archivo.

    Args:
        data_list (list): Recibe la lista con los nombres de los archivos XML.

    Returns:
        list: Retorna una lista con los archivos XML organizados de forma ascendente.
    """
    dictionary_files: dict = {}
    size_numbers: list = []
    for value in data_list:
        size = os.stat(value)
        dictionary_files.update({size.st_size: value})
        size_numbers.append(size.st_size)
    # Organiza los archivos de menor a mayor
    size_numbers.sort()
    sort_list_data = [dictionary_files[size] for size in size_numbers]
    return sort_list_data


def mkdir_folder(number: int) -> None:
    """ Función para crear carpeta en el directorio.

    Args:
        number (int): Recibe el nombre de la carpeta a crear.
    """
    os.mkdir(str(number))


# Función para mover los archivos en las carpetas creadas
def move_files(file_path: str, data_dictionary: dict) -> None:
    """ Función para mover los archivos XML a las carpetas que se les indiquen.

    Args:
        file_path (str): Recibe la ruta del directorio en donde están los archivos XML.
        data_dictionary (dict): Recibe el diccionario con los nombres de las carpetas,
        y la lista de los archivos XML.
    """
    try:
        file_counter = 0
        for folder_number in data_dictionary:
            print(print_yellow(text=f'▼ {folder_number}'))
            mkdir_folder(number=folder_number)
            for xml_file in data_dictionary[folder_number]:
                file_counter += 1
                file_size = os.stat(xml_file).st_size
                shutil.move(f"{file_path}/{xml_file}", f"{file_path}/{str(folder_number)}/{xml_file}")
                print(f"  ►{print_blue(text=xml_file)} {print_green(text='Size Bytes')} ► {print_yellow(text=str(file_size))}")
        print(f"{print_green(text='Total xml')} ► ► {file_counter} ◄ ◄")
    except Exception as error_in_move_files:
        print(print_red(text="Error en mover los archivos XML", message_Exception=error_in_move_files))


if __name__ == '__main__':
    (files, directory_path) = get_files_and_path(path=argv[1])
    data = sort_data(data_list=files)
    dictionary = organize_data(list_data=data)
    move_files(file_path=directory_path, data_dictionary=dictionary)
