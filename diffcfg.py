from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get,napalm_cli,napalm_ping,napalm_configure
from nornir_utils.plugins.functions import print_result, print_title
from nornir_utils.plugins.tasks.files import write_file
from nornir_netmiko import netmiko_send_command, netmiko_send_config
from datetime import date
from napalm import get_network_driver
from nornir.core.task import Task, Result

def pushcfg(task: Task, dry_run=True) -> Result:
    """
    Example on how to use the NAPALM to configure devices.

    If dry_run is set to True, this task will only retrieve a diff.
    """
    # print(type(task.host))
    precfg = 'precfg/' + str(task.host) + '.txt'
    napalm_ret = task.run(
        task=napalm_configure,
        dry_run=dry_run,
        filename=precfg,
        # configuration=precfg,
    )
    return Result(
        host=task.host,
        result=napalm_ret
    )

nr = InitNornir(config_file="config.yaml", dry_run=True)
r = nr.run(task=pushcfg)
print_result(r)



#
# nr = InitNornir(config_file="config.yaml", dry_run=True)
# hostname = 'sw1'
# group = nr.inventory.hosts[hostname].groups
# print(group)
# ip = nr.inventory.hosts[hostname].hostname
# usr = nr.inventory.hosts[hostname].username
# pwd = nr.inventory.hosts[hostname].password
# driver = get_network_driver(group)
# device = driver(ip, usr, pwd)
# device.open()
# device.load_replace_candidate(filename='precfg/'+hostname+'.txt')
# print(device.compare_config())
#
# try:
#     # choice = raw_input("\nWould you like to commit these changes? [yN]: ")
#     choice = input("\nWould you like to commit these changes? [yN]: ")
# except NameError:
#     choice = input("\nWould you like to commit these changes? [yN]: ")
# if choice == "y":
#     print("Committing ...")
#     device.commit_config()
# else:
#     print("Discarding ...")
#     device.discard_config()
#
# # #if you are happy with the changes:
# # device.commit_config()
# # #if you don't want to push changes:
# # device.discard_config()
#
# device.close()
#
