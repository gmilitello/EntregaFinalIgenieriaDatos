# Proyecto de Ingestión de Datos - Entrega Final

Este proyecto de ingestión de datos está diseñado para extraer información meteorológica de la ciudad de Buenos Aires desde la API de OpenWeatherMap, almacenarla en una base de datos MySQL local y luego cargarla en Amazon Redshift. Además, envía un correo electrónico de alerta si la temperatura es menor a 20°C.

## Estructura del Proyecto

El proyecto está dividido en varios módulos y archivos:

- `main.py`: Script principal que ejecuta el flujo de ingestión de datos.
- `api_extraction.py`: Módulo para extraer datos meteorológicos de la API de OpenWeatherMap.
- `mysql_extraction.py`: Módulo para extraer datos de la base de datos MySQL local.
- `redshift_transform_load.py`: Módulo para transformar y cargar datos en Amazon Redshift.
- `send_email.py`: Módulo para enviar correos electrónicos de alerta.

## Requisitos

Asegúrate de tener instalado lo siguiente antes de ejecutar este proyecto:

- Python 3.x
- pip
- PostgreSQL (para la base de datos Redshift)

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/gmilitello/EntregaFinalIngenieriaDatos.git
Accede al directorio del proyecto:
cd EntregaFinalIngenieriaDatos

Instala las dependencias:

pip install pandas requests psycopg2-binary python-dotenv sendgrid

Configura las variables de entorno:
Crea un archivo .env en el directorio raíz del proyecto.
Agrega las siguientes variables de entorno al archivo .env y proporciona los valores adecuados:
# OpenWeatherMap API Key
OPENWEATHERMAP_API_KEY=your_api_key_here

# MySQL Local Database
DB_NAME_LOCAL=your_database_name
DB_USER_LOCAL=your_database_user
DB_PASSWORD_LOCAL=your_database_password
DB_HOST_LOCAL=your_database_host
DB_PORT_LOCAL=your_database_port

# Amazon Redshift Database
DB_NAME_REDSHIFT=your_redshift_database_name
DB_USER_REDSHIFT=your_redshift_database_user
DB_PASSWORD_REDSHIFT=your_redshift_database_password
DB_HOST_REDSHIFT=your_redshift_database_host
DB_PORT_REDSHIFT=your_redshift_database_port

# SendGrid Email Configuration
SENDER_EMAIL=your_sender_email
RECEIVER_EMAIL=your_receiver_email
SENDGRID_API_KEY=your_sendgrid_api_key
Ejecución
Para ejecutar el proyecto, simplemente ejecuta el script main.py:
python main.py
Esto ejecutará el flujo de ingestión de datos, que incluye la extracción de datos del clima, la obtención de datos de la base de datos MySQL local, la transformación y carga de datos en Amazon Redshift, y el envío de un correo electrónico de alerta si la temperatura es menor a 20°C.
DAG de Airflow
El proyecto también incluye un DAG de Airflow para ejecutar el flujo de ingestión de datos de forma automatizada. Para ejecutar el DAG de Airflow, sigue estos pasos:

Accede al directorio dags:
cd dags
Activa el DAG de Airflow:
airflow dags unpause tp_final_ing_datos
