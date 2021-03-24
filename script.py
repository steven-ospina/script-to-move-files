import os
from sys import argv, exit
import shutil

# Attributes
color_green_console: str = '\33[32m'
color_blue_console: str = '\33[34m'
color_yellow_console: str = '\33[33m'
color_red_console: str = '\033[91m'
color_end_console: str = '\033[0m'
text_bold_console: str = '\33[1m'


def print_color(text: str, color: str, message_exception: Exception = '') -> str:
    """ Función para imprimir en la terminal en el color que le indiquen.

    Args:
        text (str): Recibe el texto que se va a convertir en color.
        color (str): Recibe el color que al que se va a aplicar al texto.
        message_exception (Exception)<-(optional): Recibe el mensaje de error que lance el script.

    Returns:
        str: Retorna el texto en color que hayan indicado.
    """
    if message_exception != '':
        return f"{color}{text_bold_console}{text}: {message_exception}{color_end_console}"
    else:
        return f"{color}{text_bold_console}{text}{color_end_console}"


def organize_data(list_data: list) -> dict:
    """ Función para organizar los archivos XML.

    Args:
        list_data (list): Recibe una lista con los nombres de los archivos XML.

    Returns:
        dict: Retorna un diccionario con los datos organizados por:
        {key = Número de la carpeta : value = Lista con los archivos XML }
    """
    try:
        length_list: int = len(list_data)
        if length_list <= 0:
            print(print_color(
                text="No hay archivos XML en el directorio o ya están organizados.",
                color=color_yellow_console))
            exit()
        start: int = 0
        number_of_files_first_folder: int = 5
        number_of_files_in_other_folders: int = 4
        folder: int = number_of_files_first_folder
        folder_counter: int = 0
        root_dictionary: dict = {}
        while True:
            folder_counter += 1
            formula: int = start + folder
            split_list: list = list_data[start:formula]
            if formula <= length_list:
                root_dictionary.update({folder_counter: split_list})
            else:
                end_length: int = len(split_list)
                if end_length >= 1:
                    root_dictionary.update({folder_counter: split_list})
                break
            if folder == number_of_files_first_folder:
                folder = number_of_files_in_other_folders
            start = formula
        return root_dictionary
    except Exception as error_in_organize_data:
        print(print_color(
            text="Error al organizar los archivos XML",
            color=color_red_console,
            message_exception=error_in_organize_data))


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
    cwd: str = os.getcwd()
    list_files: list = os.listdir(cwd)
    leaked_files: list = [value for value in list_files if value.endswith(".xml")]
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
    list_of_file_sizes: list = []
    for value in data_list:
        file_size: int = os.stat(value).st_size
        dictionary_files.update({file_size: value})
        list_of_file_sizes.append(file_size)
    # Organiza los archivos de menor a mayor
    list_of_file_sizes.sort()
    sort_list_data: list = [dictionary_files[size] for size in list_of_file_sizes]
    return sort_list_data


def mkdir_folder(number: int) -> None:
    """ Función para crear carpeta en el directorio.

    Args:
        number (int): Recibe el nombre de la carpeta a crear.
    """
    os.mkdir(str(number))


def move_files(file_path: str, data_dictionary: dict) -> None:
    """ Función para mover los archivos XML a las carpetas que se les indiquen.

    Args:
        file_path (str): Recibe la ruta del directorio en donde están los archivos XML.
        data_dictionary (dict): Recibe el diccionario con los nombres de las carpetas,
        y la lista de los archivos XML.
    """
    try:
        file_counter: int = 0
        for folder_number in data_dictionary:
            print(print_color(text=f'▼ {folder_number}', color=color_yellow_console))
            mkdir_folder(number=folder_number)
            for xml_file in data_dictionary[folder_number]:
                file_counter += 1
                file_size: int = os.stat(xml_file).st_size
                shutil.move(f"{file_path}/{xml_file}", f"{file_path}/{str(folder_number)}/{xml_file}")
                print_file_in_console: str = print_color(text=xml_file, color=color_blue_console)
                print_text_size: str = print_color(text='Size Bytes', color=color_green_console)
                print_size: str = print_color(text=str(file_size), color=color_yellow_console)
                print(f"  ►{print_file_in_console} {print_text_size} ► {print_size}")
        print(f"{print_color(text='Total xml', color=color_green_console)} ► ► {file_counter} ◄ ◄")
    except Exception as error_in_move_files:
        print(print_color(
            text="Error en mover los archivos XML",
            color=color_red_console,
            message_exception=error_in_move_files))


if __name__ == '__main__':
    (files, directory_path) = get_files_and_path(path=argv[1])
    data: list = sort_data(data_list=files)
    dictionary: dict = organize_data(list_data=data)
    move_files(file_path=directory_path, data_dictionary=dictionary)
