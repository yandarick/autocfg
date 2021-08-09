from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get,napalm_cli,napalm_ping,napalm_configure
from nornir_utils.plugins.functions import print_result, print_title
from nornir_utils.plugins.tasks.files import write_file
from nornir_netmiko import netmiko_send_command, netmiko_send_config
from datetime import date
from napalm import get_network_driver
from nornir.core.task import Task, Result

# def pushcfg(task: Task, dry_run=False) -> Result:
def pushcfg(task: Task, dry_run=False):
    precfg = 'precfg/' + str(task.host) + '.txt'
    r= task.run(task=napalm_configure,dry_run=dry_run,filename=precfg,)
    # return Result(host=task.host,result=r   )

nr = InitNornir(config_file="config.yaml", dry_run=True)
r = nr.run(task=pushcfg)
print_result(r)

