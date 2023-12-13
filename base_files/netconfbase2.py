from ncclient import manager
from switch_info import kwargs

config_template = open("ios_config.xml").read()

netconf_config = config_template.format(interface_name="TenGigabitEthernet1/0/1", interface_desc="Primary_uplink_trunk")

with manager.connect(host=kwargs["host"], port=kwargs["port"], username=kwargs["username"], password=kwargs["password"], hostkey_verify=False) as m:
    device_reply = m.edit_config(netconf_config, target="running")
    print(device_reply)
    