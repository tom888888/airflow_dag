from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id = "multi_task_dag",
    default_args = default_args,
    description = '測試task上限',
    start_date=datetime(2024, 4, 18),
    schedule_interval=timedelta(days=1)
) as dag:
  

    range_list=[1,2]
    with TaskGroup(group_id='multi_task') as multi_task:
    
    multi_task_list = [
        BashOperator(
            task_id=f"multi_task_{num}",
            bash_command=test_task.py,
            dag=dag)
    for num in range_list]
    multi_task_list

    multi_task
