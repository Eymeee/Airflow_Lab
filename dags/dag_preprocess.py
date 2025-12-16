from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.datasets import Dataset
from datetime import datetime

RAW_READY = Dataset("dataset://hn_raw_ready")
PROC_READY = Dataset("dataset://hn_processed_ready")

with DAG(
    dag_id="hn_preprocess",
    start_date=datetime(2024, 1, 1),
    schedule=[RAW_READY],
    catchup=False,
    tags=["preprocess"],
) as dag:
    preprocess = BashOperator(
        task_id="preprocess_hn",
        bash_command="python /opt/airflow/scripts/preprocess.py",
        outlets=[PROC_READY],
    )
