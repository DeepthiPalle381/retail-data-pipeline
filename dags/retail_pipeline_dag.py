from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Import your Python pipeline scripts
from src.ingest.ingest_data import main as ingest_main
from src.transform.transform_data import main as transform_main

default_args = {
    "owner": "deepthi",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="retail_data_pipeline",
    default_args=default_args,
    description="Daily retail pipeline: ingest -> transform -> warehouse",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["retail", "data_engineering"],
) as dag:

    ingest_task = PythonOperator(
        task_id="ingest_raw_to_clean",
        python_callable=ingest_main
    )

    transform_task = PythonOperator(
        task_id="transform_clean_to_warehouse",
        python_callable=transform_main
    )

    # Pipeline flow: ingest → transform
    ingest_task >> transform_task
