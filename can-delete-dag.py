#datetime
from datetime import timedelta, datetime

# The DAG object
from airflow import DAG

# Operators
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

# initializing the default arguments
default_args = {
		'owner': 'airflow',
		'start_date': datetime(2022, 3, 4),
		'retries': 3,
		'retry_delay': timedelta(minutes=5)
}

# Instantiate a DAG object
hello_world_dag = DAG('can_delete_dag',
		default_args=default_args,
		description='Hello World DAG',
		schedule_interval='@once', 
		catchup=False,
		tags=['example, can_delete'],
		access_control={"All": {"can_delete"}},
)

# python callable function
def print_hello():
		return 'Hello World!'
