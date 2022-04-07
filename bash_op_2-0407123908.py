from airflow.operators.bash import BashOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "bash_op_2-0407123908",
}

dag = DAG(
    "bash_op_2-0407123908",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.8.0.dev0 pipeline editor using `bash_op_2.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "url-catalog", "component_ref": {"url": "https://raw.githubusercontent.com/apache/airflow/2.2.5/airflow/operators/bash.py"}}
op_4cec7100_0a4b_4291_8369_127808ba8340 = BashOperator(
    task_id="BashOperator",
    bash_command="ls -al",
    env={},
    output_encoding="utf-8",
    skip_exit_code={"activeControl": "NumberControl", "NumberControl": 99},
    cwd="",
    dag=dag,
)
