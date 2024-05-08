from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner':'naeem',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

def get_name(ti):
    ti.xcom_push(key='first_name', value='Muhammad')
    ti.xcom_push(key='last_name', value='Naeem')

def get_age(ti):
    ti.xcom_push(key='age', value=26)

def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f"Hi, My name is {first_name} {last_name}, and I am {age} years old...")

with DAG(
    dag_id='python_operator_dag_v_7',
    description='this is my first python operator dag',
    start_date=datetime(2024, 3, 6, 1),
    schedule_interval='@daily',
    default_args=default_args
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )

    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )

    [task2, task3] >> task1
