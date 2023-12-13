from ncclient import manager
from pprint import pprint
import xml.dom.minidom
import xmltodict
import json

router = {"host": "*********", "port": "830",
          "username": "*********", "password": "********"}

netconf_filter = """
 <filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>TenGigabitEthernet1/0/1</name>
    </interface>
  </interfaces>
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>TenGigabitEthernet1/0/1</name>
    </interface>
  </interfaces-state>
</filter>
"""
with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    """
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)
    #m.close_session()
    """
    print("Connected")
    interface_netconf = m.get(netconf_filter)

    interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]
    #pprint(interface_python, sort_dicts=False)
    pprint(json.loads(json.dumps(interface_python)))

    name = interface_python['interfaces']['interface']['name']['#text']
    print(name)

    config = interface_python['interfaces']['interface']
    op_state = interface_python["interfaces-state"]["interface"]

    print("start")
    print(f"Name: {config['name']['#text']}")
    #print(f"Description: {config['description']}")
    #print(f"Packets In {op_state['statistics']['in-unicast-pkts']}")
