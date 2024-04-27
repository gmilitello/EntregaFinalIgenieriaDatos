from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from extract_api_data import extract_api_data
from extract_mysql_data import extract_mysql_data
from transform_load_redshift import transform_load_redshift
from send_email import send_email
import os
from dotenv import load_dotenv

load_dotenv()

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def main():
    city = "Buenos Aires"
    temperature = extract_api_data(city)
    extract_mysql_data()
    transform_load_redshift(city, temperature)
    if temperature < 12:
        subject = "Alerta de Temperatura"
        body = f"La temperatura en {city} es {temperature}°C, está por debajo de 12°C."
        send_email(subject, body)

with DAG('weather_data_etl_buenos_aires_dag',
         default_args=default_args,
         description='Pipeline de extracción, transformación y carga de datos del clima para Buenos Aires',
         schedule_interval='@daily',
         start_date=datetime(2024, 4, 26),
         catchup=False) as dag:

    extract_task = PythonOperator(
        task_id='extract_api_data',
        python_callable=extract_api_data,
        op_args=["Buenos Aires"]
    )

    load_task = PythonOperator(
        task_id='transform_load_redshift',
        python_callable=transform_load_redshift,
        op_args=["Buenos Aires"]
    )

    email_task = PythonOperator(
        task_id='send_email',
        python_callable=send_email
    )

    extract_task >> load_task >> email_task
