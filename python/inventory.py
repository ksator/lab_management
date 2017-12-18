def ansible_inventory_to_python_list(ansible_inv_file):
    ansible_inventory_file=open(ansible_inv_file,"r")
    ansible_inventory_string=ansible_inventory_file.read()
    ansible_inventory_file.close()

    ansible_inventory_list=ansible_inventory_string.splitlines()

    temp_list=[]
    for item in ansible_inventory_list:
        if 'junos_host' in item:
            temp_list.append(item)

    devices_list=[]
    for item in temp_list:
        devices_list.append(item.split('junos_host=')[-1])
    return devices_list


