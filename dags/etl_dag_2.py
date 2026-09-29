from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def extract():
    print("ETL 2: Extracting data...")


def transform():
    print("ETL 2: Transforming data...")


def load():
    print("ETL 2: Loading data...")


with DAG(
    dag_id="etl_dag_2",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform,
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=load,
    )

    extract_task >> transform_task >> load_task

