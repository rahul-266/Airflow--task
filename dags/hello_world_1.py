from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def hello():
    print("Hello World 1")

with DAG(
    dag_id="hello_world_1",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    hello_task = PythonOperator(
        task_id="hello_1",
        python_callable=hello,
    )
