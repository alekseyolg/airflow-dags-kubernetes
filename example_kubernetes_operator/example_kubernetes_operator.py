from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow import DAG
from datetime import datetime
import os

with DAG(
    dag_id="example_kubernetes_operator",
    schedule=None,
    start_date=datetime.now(),
    catchup=False,
    tags=["example"],
) as dag:
  example_kubernetes_operator = KubernetesPodOperator(
    name="kubernetes_operator", 
    task_id="kubernetes_operator",
    # namespace="my-namespace",
    # Specify the name of the pod template file to run on schedule
    pod_template_file=os.path.join(os.path.abspath(os.path.dirname(__file__)), 'template.yaml'),
    # It is set to be able to receive logs, since after the pod has worked and is deleted, the logs are also deleted
    # Save logs in S3
    get_logs=True,
)
# Submit for execution
example_kubernetes_operator
