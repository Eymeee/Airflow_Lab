from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.datasets import Dataset
from datetime import datetime

RAW_READY = Dataset("dataset://hn_raw_ready")

with DAG(
    dag_id="hn_scrape",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["scrape"],
) as dag:
    scrape = BashOperator(
        task_id="scrape_hn",
        bash_command="python /opt/airflow/scripts/scrape.py",
        outlets=[RAW_READY],
    )
