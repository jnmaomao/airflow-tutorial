from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "hello-generic-world-1223160034",
}

dag = DAG(
    "hello-generic-world-1223160034",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="A generic pipline tutorial",
    is_paused_upon_creation=False,
)


# Operator source: examples/pipelines/introduction-to-generic-pipelines/load_data.ipynb
op_895eba5e_252f_4743_8b40_9662b82fe9f9 = KubernetesPodOperator(
    name="Load_weather_data",
    namespace="admin",
    image="amancevice/pandas:1.1.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.3.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.3.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://192.168.30.111:9000 --cos-bucket elyra-airflows --cos-directory 'hello-generic-world-1223160034' --cos-dependencies-archive 'load_data-895eba5e-252f-4743-8b40-9662b82fe9f9.tar.gz' --file 'examples/pipelines/introduction-to-generic-pipelines/load_data.ipynb' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    task_id="Load_weather_data",
    env_vars={
        "DATASET_URL": "https://dax-cdn.cdn.appdomain.cloud/dax-noaa-weather-data-jfk-airport/1.1.4/noaa-weather-data-jfk-airport.tar.gz",
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "admin",
        "AWS_SECRET_ACCESS_KEY": "yyfwb123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "hello-generic-world-1223160034-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)


# Operator source: examples/pipelines/introduction-to-generic-pipelines/Part 1 - Data Cleaning.ipynb
op_5278dbd8_666d_4f8c_84d1_992364dbb3eb = KubernetesPodOperator(
    name="Part_1___Data_Cleaning",
    namespace="admin",
    image="amancevice/pandas:1.1.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.3.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.3.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://192.168.30.111:9000 --cos-bucket elyra-airflows --cos-directory 'hello-generic-world-1223160034' --cos-dependencies-archive 'Part 1 - Data Cleaning-5278dbd8-666d-4f8c-84d1-992364dbb3eb.tar.gz' --file 'examples/pipelines/introduction-to-generic-pipelines/Part 1 - Data Cleaning.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    task_id="Part_1___Data_Cleaning",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "admin",
        "AWS_SECRET_ACCESS_KEY": "yyfwb123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "hello-generic-world-1223160034-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_5278dbd8_666d_4f8c_84d1_992364dbb3eb << op_895eba5e_252f_4743_8b40_9662b82fe9f9
