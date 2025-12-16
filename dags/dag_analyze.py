from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.datasets import Dataset
from datetime import datetime

PROC_READY = Dataset("dataset://hn_processed_ready")

with DAG(
    dag_id="hn_analyze_hf",
    start_date=datetime(2024, 1, 1),
    schedule=[PROC_READY],
    catchup=False,
    tags=["huggingface", "analysis"],
) as dag:
    analyze = BashOperator(
        task_id="sentiment_hf",
        bash_command="python /opt/airflow/scripts/analyze_hf.py",
    )
