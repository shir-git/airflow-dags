from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from airflow.hooks.base_hook import BaseHook
from airflow.models import Variable


def get_vars(**kwargs):
  mayaya = Variable.get("mayaya", default_var=None)
  maya = Variable.get("maya", default_var=None) 
  print(f"mayaya: {mayaya}, maya: {maya}")
    
with DAG('example_variables_dags', start_date=datetime(2020, 1, 1), schedule_interval=None) as dag:

    test_task = PythonOperator(
        task_id='test-var-task',
        python_callable=get_vars
    )
