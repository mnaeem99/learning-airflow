from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime, timedelta

default_args = {
    'owner':'naeem',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='postgres_operator_dag_v_1',
    description='this is postgres operator dag',
    start_date=datetime(2024, 3, 6, 1),
    schedule_interval='@daily',
    default_args=default_args
) as dag:
    task1 = PostgresOperator(
        task_id="create_table_user",
        postgres_conn_id="postgres_local",
        sql="""
            CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL,
            age VARCHAR NOT NULL,
            dob DATE NOT NULL);
          """
    )
    
    task1
