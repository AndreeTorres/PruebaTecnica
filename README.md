# PruebaTecnica
## Descripción

La aplicación aborda una problemática común en la Universidad Centroamericana (UCA) relacionada con la falta de coordinación en los parqueos. Actualmente, se requiere mucho personal (2 por área) para coordinar los espacios disponibles, lo que resulta ineficiente y propenso a errores.

## Objetivo

El objetivo de esta aplicación es automatizar y optimizar la gestión de los espacios de estacionamiento en la UCA, reduciendo la necesidad de personal y mejorando la coordinación en la disponibilidad de espacios.

## Funcionalidades

- **Visualización en tiempo real**: Muestra el número total de espacios, los espacios disponibles y la última actualización.
- **Control de entrada y salida**: Permite registrar la entrada y salida de vehículos, actualizando automáticamente la disponibilidad de espacios.

## Tecnologías Utilizadas

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript (jQuery)
- **Base de Datos**: SQLite (puede ser reemplazada por cualquier otra base de datos soportada por Django)

## Instalación

1. Clona el repositorio:
    git clone https://github.com/AndreeTorres/PruebaTecnica.git
2. Navega al directorio del proyecto:
    cd PruebaTecnica
3. Instala las dependencias:
    pip install -r requirements.txt
4. Realiza las migraciones de la base de datos:
    python manage.py migrate
5. Ejecuta el servidor de desarrollo:
    
    python manage.py runserver
    

## Uso
1. Accede a la aplicación en tu navegador web en <Acceder de manera local>.
2. Visualiza la información del estacionamiento y utiliza los botones para registrar la entrada y salida de vehículos.
