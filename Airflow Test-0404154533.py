from airflow.operators.bash_operator import BashOperator
from airflow.operators.http_operator import SimpleHttpOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "Airflow Test-0404154533",
}

dag = DAG(
    "Airflow Test-0404154533",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.8.0.dev0 pipeline editor using `Airflow Test.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "local-file-catalog", "component_ref": {"base_dir": "/Users/jeff/tmp/elyra-ai/elyra/examples/pipelines/run-pipelines-on-apache-airflow/components", "path": "http_operator.py"}}
op_81bdc751_2c52_4de4_b30b_890144b7e65b = SimpleHttpOperator(
    task_id="SimpleHttpOperator",
    endpoint="/repos/elyra-ai/examples/contents/pipelines/run-pipelines-on-apache-airflow/resources/command.txt",
    method="GET",
    data={"ref": "master"},
    headers={"Accept": "Accept:application/vnd.github.v3.raw"},
    response_check="",
    extra_options={},
    xcom_push=True,
    http_conn_id="http_github",
    log_response=False,
    dag=dag,
)


# Operator source: {"catalog_type": "url-catalog", "component_ref": {"url": "https://raw.githubusercontent.com/elyra-ai/examples/master/pipelines/run-pipelines-on-apache-airflow/components/bash_operator.py"}}
op_0bd1ebf3_080e_4550_8717_db958318ed7a = BashOperator(
    task_id="BashOperator",
    bash_command="{{ ti.xcom_pull(task_ids='SimpleHttpOperator') }}",
    xcom_push=False,
    env={"name": "World"},
    output_encoding="utf-8",
    dag=dag,
)

op_0bd1ebf3_080e_4550_8717_db958318ed7a << op_81bdc751_2c52_4de4_b30b_890144b7e65b
