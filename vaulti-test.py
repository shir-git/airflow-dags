from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from airflow.hooks.base_hook import BaseHook
from airflow.models import Variable

#mayaya = Variable.get("mayaya")
def get_secrets(**kwargs):
    # conn = BaseHook.get_connection(kwargs['vaulti'])
    conn = BaseHook.get_connection('vaulti')
    print(f"Password: {conn.password}, Login: {conn.login}, URI: {conn.get_uri()}, Host: {conn.host}")
    print(conn)
    
with DAG('example_secrets_dags', start_date=datetime(2020, 1, 1), schedule_interval=None) as dag:

    test_task = PythonOperator(
        task_id='test-task',
        python_callable=get_secrets,
        op_kwargs={'my_conn_id': 'vaulti'},
    )
