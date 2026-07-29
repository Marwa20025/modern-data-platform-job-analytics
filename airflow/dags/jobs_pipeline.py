from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="jobs_etl_pipeline",
    start_date=datetime(2026, 7, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    extract = BashOperator(
        task_id="extract",
        bash_command="python /opt/airflow/project/producer/extract.py"
    )

    transform = BashOperator(
        task_id="transform",
        bash_command="python /opt/airflow/project/producer/transform.py"
    )

    load = BashOperator(
        task_id="load",
        bash_command="python /opt/airflow/project/producer/load.py"
    )

    extract >> transform >> load