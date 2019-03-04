
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.contrib.hooks import SSHHook
from airflow.contrib.operators.ssh_operator import SSHOperator

default_args = {
    'owner': 'sameer',
    'depends_on_past': False,
    'start_date': datetime(2019, 3, 1),
    'email': ['sameerahmad.dba@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG('create_cluster', default_args=default_args, schedule_interval=timedelta(days=1))
sshHook = SSHHook(ssh_conn_id='mymac')


t1_bash = """
/usr/bin/touch /Users/ssiddiqui/CODE/cloudera-playbook/test_file
ANSIBLE_CONFIG=/Users/ssiddiqui/CODE/cloudera-playbook/ansible.cfg /anaconda2/bin/ansible-playbook -i /Users/ssiddiqui/CODE/cloudera-playbook/ansible_hosts /Users/ssiddiqui/CODE/cloudera-playbook/site.yml
"""
# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = SSHOperator(
    task_id="task1",
    command=t1_bash,
    ssh_hook=sshHook,
    dag=dag)
