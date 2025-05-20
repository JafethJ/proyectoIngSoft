<-------------ENTORNO VIRTUAL-------------------->
1. NAVEGAR AL DIRECTORIO DONDE SE TIENE EL PROYECTO
2. CREAR EL ENTORNO VIRTUAL
    python -m venv PRO_ING

3. DARLE PERMISO DE EJCUCION DEL ARCHIVO (solo si manda error al ejecutar el archivo "activate")
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

4. ACTIVAR EL ARCHIVO "activate"
    .\PRO_ING\Scripts\activate

5. INSTALAR LAS LIBRERIAS NECESARIAS 
    pip install flask      (Obligatorio)

<--------------------CORRER LA WEB--------------------->
Para compilar la web, se debe realizar desde el archivo run.py, 
a. teniendo xampp encendido, apache y MySQL
b. el entorno virtual encendido

<------------------TRABAJAR CON LA BD------------------>
pip install flask-sqlalchemy pymysql


