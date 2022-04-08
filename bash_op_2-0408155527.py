from airflow.providers.papermill.operators.papermill import PapermillOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "bash_op_2-0408155527",
}

dag = DAG(
    "bash_op_2-0408155527",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.8.0.dev0 pipeline editor using `bash_op_2.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "airflow-provider-package-catalog", "component_ref": {"provider_package": "apache_airflow_providers_papermill-2.2.3-py3-none-any.whl", "provider": "apache_airflow_providers_papermill", "file": "airflow/providers/papermill/operators/papermill.py"}}
op_b307914a_f810_4155_a17e_d43bb3715060 = PapermillOperator(
    task_id="My_NB",
    input_nb="bob.ipynb",
    output_nb="out.ipynb",
    parameters={},
    kernel_name=None,
    dag=dag,
)
