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
can_read_dag = DAG('can_read_permission_only',
		default_args=default_args,
		description='Can read permission dag',
		schedule_interval='@once', 
		catchup=False,
		tags=['example, can read'],
		access_control={
		'auto_user': {
			'can_read'
		}
	}
)

# python callable function
def print_hello():
		return 'Hello World!'
