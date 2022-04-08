from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.providers.papermill.operators.papermill import PapermillOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "bash_op_2-0408173419",
}

dag = DAG(
    "bash_op_2-0408173419",
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


# Operator source: {"catalog_type": "airflow-provider-package-catalog", "component_ref": {"provider_package": "apache_airflow_providers_snowflake-2.6.0-py3-none-any.whl", "provider": "apache_airflow_providers_snowflake", "file": "airflow/providers/snowflake/operators/snowflake.py"}}
op_98032001_5c8d_4ecf_8aa2_b91cb1ccd585 = SnowflakeOperator(
    task_id="SnowflakeOperator",
    sql="Select * from table",
    snowflake_conn_id="snowflake_default",
    parameters={},
    autocommit=True,
    do_xcom_push=True,
    warehouse=None,
    database=None,
    role=None,
    schema=None,
    authenticator=None,
    session_parameters={},
    dag=dag,
)

op_98032001_5c8d_4ecf_8aa2_b91cb1ccd585 << op_b307914a_f810_4155_a17e_d43bb3715060


# Operator source: examples/pipelines/run-generic-pipelines-on-apache-airflow/Part 1 - Data Cleaning.ipynb
op_30ca4eae_93b1_4af1_a9c0_d687402c864b = KubernetesPodOperator(
    name="Part_1___Data_Cleaning",
    namespace="admin",
    image="amancevice/pandas:1.4.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/master/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/master/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://localhost:9000 --cos-bucket elyra-test --cos-directory 'bash_op_2-0408173419' --cos-dependencies-archive 'Part 1 - Data Cleaning-30ca4eae-93b1-4af1-a9c0-d687402c864b.tar.gz' --file 'examples/pipelines/run-generic-pipelines-on-apache-airflow/Part 1 - Data Cleaning.ipynb' "
    ],
    task_id="Part_1___Data_Cleaning",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "bash_op_2-0408173419-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_30ca4eae_93b1_4af1_a9c0_d687402c864b << op_b307914a_f810_4155_a17e_d43bb3715060
