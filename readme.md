# Proyecto de Descarga de Archivos Excel en el Cliente con Paginación

Este proyecto es una prueba de concepto que demuestra cómo descargar archivos Excel en el cliente utilizando JavaScript y la biblioteca SheetJS, con soporte de paginación para manejar grandes conjuntos de datos.

El objetivo de este proyecto es mostrar cómo generar y descargar archivos Excel directamente en el cliente, evitando la carga excesiva en el servidor y mejorando la velocidad de respuesta mediante la implementación de la paginación.

## Cómo usar

1. Clona o descarga este repositorio en tu máquina local.

2. Asegúrate de tener Django y las dependencias necesarias instaladas. Puedes instalar las dependencias ejecutando el siguiente comando:

```pip install -r requirements.txt```


3. Crea una base de datos y configura la conexión en el archivo `settings.py` de Django.

4. Realiza las migraciones para crear las tablas de la base de datos ejecutando los siguientes comandos:

```
python manage.py makemigrations
python manage.py migrate
```


5. Opcionalmente, si deseas crear más datos de prueba, puedes ejecutar el siguiente comando para generar registros ficticios en la base de datos:

```python manage.py dummy_data <num_registros>```


Donde `<num_registros>` es el número de registros de prueba que deseas crear en la tabla `DummyData`. Por ejemplo, para crear 20000 registros, puedes ejecutar:

```python manage.py dummy_data 20000```


6. Inicia el servidor de desarrollo de Django con el siguiente comando:

```python manage.py runserver```


7. Abre tu navegador web y accede a la siguiente URL: `http://localhost:8000/`.

Verás una página con un botón "Descargar Excel". Haz clic en el botón para comenzar la descarga de los datos en un archivo Excel.

- Si hay una gran cantidad de datos, se utilizará la paginación para dividir los datos en páginas más pequeñas y descargar múltiples archivos Excel en el cliente.
- Cada archivo Excel descargado contendrá una página de datos.
- Los archivos Excel se generarán directamente en el cliente utilizando JavaScript y la biblioteca SheetJS.

8. Si deseas ajustar el tamaño de la página (número de registros por página), puedes modificar el valor de `pageSize` en el archivo `index.html`.

9. Para personalizar el proyecto según tus necesidades, puedes explorar y modificar los siguientes archivos:

- `dummyapp/models.py`: Define el modelo `DummyData` que representa los datos utilizados en el proyecto.
- `dummyapp/views.py`: Contiene la lógica de la vista que maneja las solicitudes AJAX y la generación de archivos Excel en el servidor.
- `dummyapp/templates/index.html`: Plantilla HTML que muestra el botón de descarga y contiene el código JavaScript para realizar las solicitudes AJAX y generar los archivos Excel en el cliente.

## Licencia

Este proyecto se distribuye bajo la licencia [MIT](LICENSE).
