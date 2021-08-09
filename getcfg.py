from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result, print_title
from nornir_utils.plugins.tasks.files import write_file
from nornir_netmiko import netmiko_send_command, netmiko_send_config
from datetime import date

nr = InitNornir(config_file="config.yaml", dry_run=True)

def backup_configurations(task):
    r = task.run(task=napalm_get, getters=["config"])
    task.run(task=write_file, content=r.result["config"]["running"],
             filename= 'runcfg/'+ str(task.host.name)+ "_" + "running" + "_" + str(date.today()) + ".txt")

    task.run(task=write_file, content=r.result["config"]["startup"],
             filename= 'runcfg/'+ str(task.host.name) + "_" + "startup" + "_" + str(date.today()) + ".txt")

nr = InitNornir(config_file="config.yaml")
result = nr.run(name="Backup Configuration", task=backup_configurations)

print_result(result)
