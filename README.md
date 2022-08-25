## Prueba DataQU

Aplicacion Web para arriendos y autos y administración, desarrollada en Django.

1) inicialmente se debe crear las migraciones y que se genere la base de datos en SQLite3

```sh
python manage.py makemigrations

python manage.py migrate
```


2) para poder cargar los datos, se ejecuta el siguiente archivo data.py

```sh
python data.py
```


3) Como pantalla principal se muestra un dashboard con la información de Arriendos
y sus graficos. 


![Alt text](/images/dashbard.jpg)



4) para ver el formulario de ingreso de Arriendo

![Alt text](/images/insert.jpg)
