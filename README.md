# Call Center

Permite hacer un control del registro de llamdas de atención al cliente

    - Usuario con estatus de superusuario puede realizar cualquier acción en el panel administrativo
    - Usuario con rol Supervisor puede registrar agentes y ver el registro de atención al cliente
    - usuario con rol Agente puede hacer el registro de atención al cliente
    - Usuario con rol Analista puede ver el registro de atención al cliente

## Pasos para crear el entorno de desarrollo

Cuando somos un usuario normal del sistema, en el terminal se mostrará el siguiente símbolo: ~$

Cuando accedemos al usuario root del sistema, en el terminal se mostrará el siguiente símbolo: ~#

Probado en últimas versiones estables de Debian y Ubuntu. Instalar los siguientes programas

    ~# apt install curl git graphviz graphviz-dev phppgadmin postgresql python3-dev virtualenv

Crear las siguientes carpetas

    ~$ mkdir Programación

Desde el terminal, moverse a la carpeta Programación y ejecutar

    ~$ cd Programación/

    ~$ mkdir python

Entrar a la carpeta python y hacer lo siguiente

    ~$ cd python/

    ~$ mkdir entornos_virtuales proyectos_django

Entrar a entornos_virtuales

    ~$ cd entornos_virtuales/

    ~$ mkdir django

Desde el terminal, moverse a la carpeta django y ejecutar

    ~$ cd django/

    ~$ virtualenv -p python3 call_center

Para activar el entorno

    ~$ source call_center/bin/activate

Nos movemos a la carpeta proyectos_django, descargamos el sistema y entramos a la carpeta con los siguientes comandos

    (call_center) ~$ cd ../../proyectos_django/

    (call_center) ~$ git clone https://github.com/willez88/call_center.git

    (call_center) ~$ cd call_center/

    (call_center) ~$ cp call_center/settings.default.py call_center/settings.py

    (call_center) ~$ mkdir db

Tendremos las carpetas estructuradas de la siguiente manera

    // Entorno virtual
    Programación/python/entornos_virtuales/django/call_center

    // Servidor de desarrollo
    Programación/python/proyectos_django/call_center

Crear la base de datos para __call_center__ usando PostgresSQL

    // Acceso al usuario postgres
    ~# su postgres

    // Acceso a la interfaz de comandos de PostgreSQL
    postgres@xxx:$ psql

    // Creación del usuario de a base de datos
    postgres=# CREATE USER admin WITH LOGIN ENCRYPTED PASSWORD '123' CREATEDB;
    postgres=# \q

    // Desautenticar el usuario PostgreSQL y regresar al usuario root
    postgres@xxx:$ exit

    // Salir del usuario root
    ~# exit

Puedes crear la base de datos colocando en el navegador: localhost/phppgadmin

    // Nombre de la base de datos: call_center

Instalamos los requemientos que el sistema necesita en el entorno virtual

    (call_center) ~$ pip install -r requirements/dev.txt

Hacer las migraciones

    (call_center) ~$ python manage.py makemigrations base users

    (call_center) ~$ python manage.py migrate

    (call_center) ~$ python manage.py loaddata groups 1_projects 2_dispositions 3_subdispositions call_results client_types

Crear usuario administrador

    (call_center) ~$ python manage.py createsuperuser

Correr el servidor de django

    (call_center) ~$ python manage.py runserver

Poner en el navegador la url que sale en el terminal para entrar el sistema

Llegado hasta aquí el sistema ya debe estar funcionando

Para salir del entorno virtual se puede ejecutar desde cualquier lugar del terminal: deactivate

Generar gráfico del modelo Entidad-Relación

    // Grafica el modelo entidad-relación del proyecto
    (call_center) ~$ python manage.py graph_models -a -g -o call_center.svg

    // Grafica el modelo de una app del proyecto
    (call_center) ~$ python manage.py graph_models base -g -o base.svg

Estilo de codificación PEP 8 en Visual Studio Code

    // Abre el proyecto con vscode
    (call_center) ~$ code .

    Ir a extensiones del vscode e instalar
        ruff
        isort
        Python Environment Manager

    Python Environment Manager detectará todos los entornos virtuales creados
    en la sección Venv, click en "Set as active workspace interpreter" para activarlo

    Para que los cambios hagan efecto cerrar el vscode y abrirlo de nuevo

Exportar base de datos usando Django

    // Respaldo completo de los datos
    (call_center) ~$ python manage.py dumpdata --indent 4 > db/call_center_prod.json

Importar base de datos usando Django

    // Resetear base de datos
    (call_center) ~$ python manage.py reset_db

    // Eliminar las migraciones del proyecto
    (call_center) ~$ find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

    // Eliminar los archivos compilados
    (call_center) ~$ python manage.py clean_pyc

    // Ejecutar
    (call_center) ~$ python manage.py makemigrations base users
    
    (call_center) ~$ python manage.py migrate

    // Luego entrar al gestor de base de datos
    //conectarse a la base de datos
    postgres=# \c call_center

    // Vaciar las siguientes tablas para que no generen conflicto cuando se importen los datos
    call_center=# TRUNCATE TABLE auth_permission CASCADE;
    call_center=# TRUNCATE TABLE django_content_type CASCADE;

    // Por último importar call_center_prod.json
    (call_center) ~$ python manage.py loaddata db/call_center_prod.json
