# Instalación

El sistema fue desarrollado para ser utilizado con MySQL, es por esto que debe tener instalado el mismo.

### 1er Paso - Clonar repositorio

Para este paso lo que se debe obtener es la clave SSH del repositorio, para esto debe dirigirse a la siguiente URL 
(https://github.com/YagoMaureira/Tickets-Soporte.git), dirigirse al boton donde dice **Code**, luego dirigirse a la 
pestaña con el nombre **SSH** y copiar la clave. Luego en la terminal debe ingresar lo siguiente: 

```sh
$ git clone (clave SSH)
```

Una vez hecho esto, debería clonarse el repositorio dentro de un directorio llamado **Tickets-Soporte**.

### 2do Paso - Crear entorno Virtual

Dentro del directorio **/Tickets-Soporte**, por terminal deberá ingresar lo siguiente para generar el entorno virtual:

```sh
$ virtualenv venv 
```

Con esto quedara creado el entorno virtual para la utilización del sistema

## 3er Paso - Instalación de librerías

Como primera instancia se debe activar el entorno virtual para la instalacion de las librerías a utilizar, para esto en
la terminal y dentro del directorio **/Tickets-Soporte** debe ejecutar lo siguiente:

```sh 
$ source venv/bin/activate
```

Hecho esto, se activará el entorno virtual y podremos instalar las librerias requeridas. Para la instalación de las
librerías en la terminal ingrese lo siguiente:
```sh
$ pip3 install -r requirements.txt
```

Con esta linea ingresada en terminal y con el entorno activado, se instalarán las librerías en este último.

### 4to Paso - Creación de modelos en la base de datos

En primera instancia, se debe configurar la conexion a la base de datos, es por esto que se debe crear un arhivo
**.env**, en donde se encontrarán las credenciales para la conexión a su base de datos y que se puedan almacenar los
tickets posteriormente. Para crear dicho arhivo, dentro del directorio **Tickets-Soporte**, en terminal se debe 
ingresar:

```sh 
$ touch .env
```

De esta manera quedará creado el archivo requerido y da inicio a la segunda instancia en donde debe colocar las
credenciales para la conexion a la base de datos, las credenciales deben ir dentro del archivo .env de la siguiente
forma:

```
export DB_USER=(Usuario Base de Datos)
export DB_PASS=(Contraseña de la Base de Datos)
export DB_NAME=(Nombre del schema en donde se creará la tabla correspondiente al modelo del ticket)
``` 

Dentro de los parentesis **()** debe ingresar los datos requeridos.

En este punto se debe crear el modelo de ticket en la base de datos. Con el entorno virtual activado, y a través de la 
terminal debe ejecutar el siguiente archivo de python:

```sh 
$ python3 models.py
```

Una vez ejecutado lo anterior, se deberia crear en el correspondiente schema la tabla **tickets**.
Con todos los pasos realizados de manera correcta, el sistema queda listo para su utilización.