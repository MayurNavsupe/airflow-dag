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
}

# Instantiate a DAG object
hello_world_dag = DAG('run_once_dag_admin',
		default_args=default_args,
		description='Hello World DAG',
		schedule_interval='@once', 
		catchup=False,
		tags=['example, helloworld'],
		access_control={"qa1": {"can_read", "can_edit", "can_delete"}},
)

# python callable function
def print_hello():
		return 'Hello World!'
