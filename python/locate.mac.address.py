'''
python script to find where is a mac address
it uses the ansible inventory file, login in all the device, and print where the mac address is.
'''
'''
works wit QFX 5100 and 5110 and 10K. works with EX4550. doesnt yet work with SRX. 
'''
'''
python ./python/locate.mac.address.py 38:4f:49:f2:5f:fc
'''
from jnpr.junos import Device
from jnpr.junos.exception import *
from lxml import etree
from pprint import pprint
import sys


from inventory import ansible_inventory_to_python_list
devices_list=ansible_inventory_to_python_list('hosts')

from  credentials import ansible_credentials_to_python_credentials
user = ansible_credentials_to_python_credentials()['user']
password = ansible_credentials_to_python_credentials()['password']


for dev_item in devices_list:
    dev=Device(host=dev_item, user=user, password=password)
    try:
        dev.open()
    except ConnectRefusedError:
        print("")
        print"python can not connect to the device %s" %(dev_item)
    except :
        print("")
        print "python faced another pyez exception trying to open a connection with the device %s" %(dev_item)
    else:
        if 'SRX' in dev.facts['model']: 
            print("")
            print "the device %s is an %s model, and this script doesnt yet support %s model" %(dev.facts['hostname'], dev.facts['model'], dev.facts['model'])
        elif dev.facts['model'] != 'EX4550-32F':
            interface_list=[]
            result=dev.rpc.get_ethernet_switching_table_information(normalize=True, address=sys.argv[1])
            mac_list = result.findall('l2ng-l2ald-mac-entry-vlan/l2ng-mac-entry')
            if len (mac_list) == 0:
                print("")
                print "%s is not known by %s" %(sys.argv[1], dev.facts['hostname'])
                dev.close()
            else:
                for mac_item in mac_list:
                    if  mac_item.findtext('l2ng-l2-mac-logical-interface') not in interface_list:
                        interface_list.append(mac_item.findtext('l2ng-l2-mac-logical-interface'))
                print("")
                print "%s is known by %s via the list of interfaces %s" %(sys.argv[1], dev.facts['hostname'],  interface_list)
                dev.close()
        elif dev.facts['model'] == 'EX4550-32F': 
            interface_list=[]
            result=dev.rpc.get_ethernet_switching_table_information(normalize=True)
            mac_list = result.findall('ethernet-switching-table/mac-table-entry')
            for item in mac_list: 
                if sys.argv[1] in item.findtext('mac-address'): 
                     if item.findtext('mac-interfaces-list/mac-interfaces') not in interface_list: 
                         interface_list.append(item.findtext('mac-interfaces-list/mac-interfaces'))
            if len (interface_list) == 0:
                print("")
                print "%s is not known by %s" %(sys.argv[1], dev.facts['hostname'])
                dev.close()
            else:
                print("")
                print "%s is known by %s via the list of interfaces %s" %(sys.argv[1], dev.facts['hostname'],  interface_list)
                dev.close()
devices_list_size=len(devices_list)
print("")
print "lookup done accross %s devices." %devices_list_size

