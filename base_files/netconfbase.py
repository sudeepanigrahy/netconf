from ncclient import manager
import xml.dom.minidom

router = {"host": "*********", "port": "830",
          "username": "********", "password": "*********"}

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
    #get() will bring you both the operational and configurational data
    #get_config() will bring you only the configurational data
    
    #interface_netconf = m.get_config('running', netconf_filter)    
    interface_netconf = m.get(netconf_filter)
    #print(interface_netconf)

    xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
    print(xmlDom.toprettyxml(indent=" "))
    print('*'*25 + 'Break' + '*'*50)
    m.close_session()
    
