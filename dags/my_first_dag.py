from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner':'naeem',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='my_first_dag_v_2',
    description='this is my first dag',
    start_date=datetime(2024, 3, 6, 1),
    schedule_interval='@daily',
    default_args=default_args
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo Hello, first task!",
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo Hello, second task!",
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command="echo Hello, third task!",
    )

    task1.set_downstream(task2)
    task1.set_downstream(task3)

