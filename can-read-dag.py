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
hello_world_dag = DAG('can_read_permission_only',
		default_args=default_args,
		description='Can read permission dag',
		schedule_interval='@once', 
		catchup=False,
		tags=['example, can read'],
		access_control={
		'role_member': {
			'can_read',
			'can_edit',
			'can_delete'
		}
	}
)

# python callable function
def print_hello():
		return 'Hello World!'
