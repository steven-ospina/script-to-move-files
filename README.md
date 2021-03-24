# script-to-move-files

![dependencies](https://img.shields.io/badge/python-v3.6.9-blue.svg)
![Current Version](https://img.shields.io/badge/version-1.1.4-green.svg)

Este script está diseñado para crear carpetas en orden numérico y mover los archivos en las carpetas creadas.

## Tabla de contenido

- [script-to-move-files](#script-to-move-files)
  - [Tabla de contenido](#tabla-de-contenido)
  - [Instalar Python 3](#instalar-python-3)
    - [Procedemos a instalar Python3 en la distribución de Linux Ubuntu](#procedemos-a-instalar-python3-en-la-distribución-de-linux-ubuntu)
      - [1 - Actualizamos las dependencias y paquetes del sistema](#1---actualizamos-las-dependencias-y-paquetes-del-sistema)
      - [2 - Comprobamos la versión del Python 3](#2---comprobamos-la-versión-del-python-3)
      - [2 - Instalamos Python 3 en el sistema](#2---instalamos-python-3-en-el-sistema)
  - [Configuración](#configuración)
    - [Como usar la aplicación](#como-usar-la-aplicación)
      - [Comando para mover los archivos XML](#comando-para-mover-los-archivos-xml)
    - [Correr aplicación con bash o zsh](#correr-aplicación-con-bash-o-zsh)
      - [Configurar .bashrc_aliases o .zshrc_aliases](#configurar-bashrc_aliases-o-zshrc_aliases)
      - [Ejemplos de como utilizar el script con bash](#ejemplos-de-como-utilizar-el-script-con-bash)
  - [Licencia](#licencia)

## Instalar Python 3

Para poder ejecutar el proyecto se necesita instalar **Python 3** y es recomendable correr la aplicación en el sistema operativo Linux.

### Procedemos a instalar Python3 en la distribución de Linux Ubuntu

#### 1 - Actualizamos las dependencias y paquetes del sistema

- **Ejecutamos en la terminal el siguiente comando para actualizar el sistema Linux**

```shell
sudo apt-get update
```

- **Instalamos las dependencias y paquetes descargados**

```shell
sudo apt-get upgrade
```

- **Confirme la instalación si se le solicita.**

#### 2 - Comprobamos la versión del Python 3

- **Compruebe qué versión de Python 3 tiene instalada el sistema escribiendo:**

```shell
python3 -V
```

**Otra forma de saber la versión de Python.**

```shell
python3 --version
```

> **En caso de que el sistema no imprima la versión del Python procedemos instalarlo**

#### 2 - Instalamos Python 3 en el sistema

- Ya con el sistema operativo actualizado procedemos instalar en la terminal el Python 3 y ejecutamos el siguiente comando:

```shell
sudo apt install python3
```

> **Confirme la instalación del python3 y al terminar ya podremos saber la versión instalada**

## Configuración

Clone esté repositorio con el siguiente comando en la terminal:

```shell
git clone https://github.com/steven-ospina/script-to-move-files.git
```

### Como usar la aplicación

Después de clonar este repositorio en su directorio, nos movemos al proyecto ejecuté el siguiente comando:

```shell
cd script-to-move-files/
```

> Ya estando en la raíz del proyecto podremos ejecutar los comandos que tiene la aplicación.

#### Comando para mover los archivos XML

Ejecutando el siguiente comando podremos crear las carpetas en orden numérico y mover los archivos XML a las carpetas creadas por el script:

```shell
python3 script.py PATH_WITH_XML_FILES/
```

Ejecutando el comando anterior en la terminal y si funciona correctamente aparecerá lo siguiente:

```shell
▼ 1
  ►Archivo1.xml Size Bytes ► 1746
  ►Archivo2.xml Size Bytes ► 2175
  ►Archivo3.xml Size Bytes ► 2226
  ►Archivo4.xml Size Bytes ► 3218
  ►Archivo5.xml Size Bytes ► 9997
▼ 2
  ►Archivo6.xml Size Bytes ► 1746
  ►Archivo7.xml Size Bytes ► 2175
  ►Archivo8.xml Size Bytes ► 2226
  ►Archivo9.xml Size Bytes ► 3218
Total xml ► ► 9 ◄ ◄
```

>**Ejemplo de como se imprime en la terminal cuando se mueven los archivos XML.**

**NOTA:** Por necesidad de la creación del script, tiene como regla que la primera carpeta debe alojar la cantidad máxima de `5` archivos y el resto de carpetas la cantidad de `4` archivos, pero sí en la carpeta hay menos, el script también puede crear las carpetas y mover los archivos con normalidad.

### Correr aplicación con bash o zsh

Creando los alias en `.bash_aliases` o `.zsh_aliases` podremos ejecutar la aplicación sin la necesidad de poner el comando `python3` antes de ejecutar la aplicación, además otras ventajas que tiene de ejecutar la aplicación es que se puede configurar para poder ejecutar la aplicación en cualquier parte del sistema Linux, y seguirá recibiendo los mismos parámetros que recibe si lo estuviera tirando desde el directorio raíz, para configurar esté archivo debemos seguir las siguientes instrucciones:

#### Configurar .bashrc_aliases o .zshrc_aliases

No dirigimos al `$HOME` de Linux `~$:` donde están los archivos `.bashrc` o `.zshrc` y con un editor de texto como `vim` o `nano`, nos dirigimos casi al final del archivo, y el archivo debe tener las siguientes líneas de código:

`.bashrc`

```bash
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
```

**En `.zshrc` debes crear estas líneas de código:**

```zsh
if [ -f ~/.zsh_aliases ]; then
    . ~/.zsh_aliases
fi
```

Ya verificando que están estas líneas de código podremos agregar la aplicación en el archivo `.bashrc_aliases` o `.zshrc_aliases`, y lo hacemos de la siguiente manera, agregando estas líneas de código:

```zsh
# Ejecutar la aplicación script-to-move-files
alias script-mv-xml="python3 /home/USER-linux/ruta-donde-clonó-el-repositorio/script-to-move-files/script.py"
```

> Al final de la ruta debemos poner el nombre del archivo `script.py` para poder ejecutar la aplicación por medio de `BASH`, y también recuerda poner `python3` antes de la ruta para que se pueda ejecutar el script.

Cuando hayas agregado el alias, debes guardar el archivo y luego ejecutar el siguiente comando para que Linux pueda reconocer la aplicación en el sistema y el comando sería:

```zsh
# Ejecutar aplicación script-to-move-files
source .bashrc
o
source .zshrc
```

Si todo sale bien, en la terminal no debe aparecer nada y para verificar que quedo cargada en el sistema podemos ejecutar el siguiente comando:

```zsh
alias | grep script-mv-xml
```

**Y en la terminal nos mostrará el alias con la ruta del script que agregaste.**

#### Ejemplos de como utilizar el script con bash

Ya con haber configurado seguido los pasos anteriores, te muestro un ejemplo de como utilizar la aplicación por medio del `bash` y este es el ejemplo:

```zsh
# Con este comando mueves los archivos XML a las carpetas que crea el script.
script-search-xml PATH_WITH_XML_FILES/
```

## Licencia

>Puede consultar la licencia completa [aquí](LICENSE)

Este proyecto tiene la licencia de acuerdo con los términos de la licencia del **MIT**.
