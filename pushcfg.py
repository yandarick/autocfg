from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get,napalm_cli,napalm_ping
from nornir_utils.plugins.functions import print_result, print_title
from nornir_utils.plugins.tasks.files import write_file
from nornir_netmiko import netmiko_send_command, netmiko_send_config
from datetime import date

hostname = 'sw1'

nr = InitNornir(config_file="config.yaml", dry_run=True)

def config(cisco):
    cisco.run(task=netmiko_send_config, config_file='precfg/'+hostname+'.txt')
    cisco.run(task=netmiko_send_command, command_string='show run interface g0/10')
results = nr.run(task=config)
config_file='precfg/'+hostname+'.txt'
print_result(results)
