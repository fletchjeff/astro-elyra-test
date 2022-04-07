from airflow.operators.bash import BashOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "bash_op_2-0407120927",
}

dag = DAG(
    "bash_op_2-0407120927",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.8.0.dev0 pipeline editor using `bash_op_2.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "url-catalog", "component_ref": {"url": "https://raw.githubusercontent.com/apache/airflow/main/airflow/operators/bash.py"}}
op_f0427bc5_0121_4067_abf2_5c6d65efc33c = BashOperator(
    task_id="BashOperator",
    bash_command="ls -al",
    env={},
    append_env=False,
    output_encoding="utf-8",
    skip_exit_code={"activeControl": "NumberControl", "NumberControl": 99},
    cwd="",
    dag=dag,
)
