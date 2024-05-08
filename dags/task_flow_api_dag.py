
from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {
    'owner':'naeem',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


@dag(
    dag_id='task_flow_api_dag_v2',
    description='this is a task flow api dag',
    start_date=datetime(2024, 3, 6, 1),
    schedule_interval='@daily',
    default_args=default_args
) 

def great_etl():

    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'M.',
            'last_name': 'Naeem'
        }
    
    @task()
    def get_age():
        return 25
    
    @task()
    def greet(first_name, last_name, age):
        print(f"Hi, My name is {first_name} {last_name}, and I am {age} years old...")
    
    name = get_name()
    age = get_age()
    greet(name['first_name'], name['last_name'], age)



great_dag = great_etl()
