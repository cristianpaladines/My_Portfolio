# My_Portfolio with Django

![image](https://user-images.githubusercontent.com/112832288/219879921-40e32a9e-fad8-47a6-a6c0-51ad349d4b0b.png)


Este es un proyecto de portafolio personal construido principalmente con Django, en el que se muestra información acerca de mi experiencia, habilidades y algunos proyectos.

# Requerimientos del sistema
Para ejecutar correctamente este proyecto, se requiere lo siguiente:

- Python 3.10 o superior
- Django 4.1 o superior
- Otros requerimientos se encuentran en el archivo requirements.txt.

# Instalación y configuración
Primero se debe clonar este repositorio en tu máquina local con el comando git clone https://github.com/cristianpaladines/My_Portfolio.git

Luego se debe abrir una terminal en el directorio donde se clonó el repositorio y cree un entorno virtual de Python con el comando python3 -m venv env. Luego, se activa el entorno virtual con el comando source env/bin/activate (en Unix/MacOS) o env\Scripts\activate (en Windows).

Instalar las dependencias necesarias con el comando:
```
pip install -r requirements.txt
```
Realizar las migraciones de la base de datos con el comando:
```
python manage.py migrate
```
Crear un superusuario para acceder al panel de administración de Django con el comando:
```
python manage.py createsuperuser
```
Finalmente, iniciar el servidor web local con el comando: 
```
python manage.py runserver
```
y abrir el navegador web en http://localhost:8000 para ver la aplicación.

# Uso

Este proyecto muestra información sobre mi experiencia, habilidades y proyectos en los que he trabajado.
Para acceder al panel de administración de Django, se debe iniciar sesión con las credenciales del superusuario que se crearon anteriormente en http://localhost:8000/admin.

# Contribución

Si desea contribuir a este proyecto, por favor sigue los siguientes pasos:

Haz un fork de este repositorio.

Crea una rama nueva para tus cambios con el comando git checkout -b nombre-de-tu-rama.

Realiza los cambios necesarios y haz commit de tus cambios con mensajes descriptivos.

Envía un pull request a este repositorio para revisión.

# Autor: Cristian Camilo Paladines
