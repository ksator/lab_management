# Repository documentation structure

- [**What to find in this repository**](README.md#what-to-find-in-this-repository)
- [**Requirements to use this repository**](README.md#requirements-to-use-this-repository)
- [**source of truth**](README.md#source-of-truth) 
- [**How to locate a mac address in the network**](README.md#how-to-locate-a-mac-address-in-the-network)
- [**How to collect data from the network**](README.md#how-to-collect-data-from-the-network) 
- [**How to configure the network**](README.md#how-to-configure-the-network)
- [**How to audit the network with Ansible**](README.md#how-to-audit-the-network-with-ansible)
- [**How to audit the network using JSNAPy**](README.md#how-to-audit-the-network-using-jsnapy)
- [**Repository structure**](README.md#repository-structure)
- [**Looking for help**](README.md#looking-for-help)


# What to find in this repository

Junos automation content for data center network fabric.  
It is used to manage a lab.  
It is based on:    
- Junos devices
- Ansible, PyEZ, JSNAPy

# Requirements to use this repository

### Install PyEZ, Ansible, JSNAPy

This repository has been tested using Ansible 2.4.2.0  

Run these commands on Ubuntu 16.04 to install these tools:
```
sudo -s
apt-get update
apt-get install -y python-dev libxml2-dev python-pip libxslt1-dev build-essential libssl-dev libffi-dev git
pip install junos-eznc jxmlease wget jsnapy ansible==2.4.2.0 requests ipaddress cryptography==1.2.1 
ansible-galaxy install Juniper.junos
```
Check the Ansible version:
```
ansible --version
```
Verify you have the Juniper.junos role: 
```
ls /etc/ansible/roles/
```
This repository has been tested using the version 1.4.3 of the Juniper.junos role available on Galaxy.  
Use this command to see the name and version of each role installed:
```
ansible-galaxy list
```

### Get locally the content of the remote repository

```
sudo -s
git clone http://172.25.90.133/root/PoC-80.git
ls PoC-80/
```

### Move to the local copy of the remote repo

```
cd PoC-80/
sudo -s
```

You can now use the local copy of this remote repository.  
You need to run the below commands within the root of the project tree.

# source of truth

This repository uses Ansible, PyEZ and JSNAPy.  
Ansible is the source of truth for the inventory and the credentials, so: 
- [**JSNAPy inventory file**](jsnapy/testfiles/devices.yml) is created automatically (using this [**playbook**](pb.generate.jsnapy.inventory.yml) and [**template**](/templates/jsnapy_inventory.j2)), based on the [**Ansible inventory file**](hosts) and based on the [**Ansible variables for devices credentials**](/group_vars/JUNOS/credentials.yml)
- Devices list for PyEZ is created automatically based on the [**Ansible inventory file**](hosts) (using this [**python script**](/python/inventory.py)). In addition, using this [**python script**](/python/credentials.py), PyEZ is able to reuse the [**Ansible variables for devices credentials**](/group_vars/JUNOS/credentials.yml).


# How to locate a mac address in the network
Execute this [**python script**](python/locate.mac.address.py) to locate a mac address in the network
```
python ./python/locate.mac.address.py 38:4f:49:f2:5f:fc
```

# How to collect data from the network 

### How to pass show commands on junos devices and collect the commands output
Edit the [**cli.yml**](cli.yml) file to indicate the list of junos show commands you want to use
```
vi cli.yml
```

Run this command to execute the [**pb.collect.cli.output.yml**](pb.collect.cli.output.yml) playbook.  
It runs the junos show commands from the [**cli.yml**](cli.yml) file and save the output on the Ansible server in the [**cli**](cli) directory. 
```
ansible-playbook pb.collect.cli.output.yml
```

The junos show commands output is available in the [**cli**](cli) directory 
```
ls cli
```

### How to pass show commands on junos devices and collect the output (alternative automation content)
Edit the [**pb.collect.commands.output.yml**](pb.collect.commands.output.yml) file to indicate the list of junos show commands you want to use
```
vi pb.collect.commands.output.yml
```

Run this command to execute the [**pb.collect.commands.output.yml**](pb.collect.commands.output.yml) playbook.  
It runs the junos show commands and save the output on the Ansible server in the [**command**](command) directory. 
```
ansible-playbook pb.collect.commands.output.yml
```

The commands output is available in the [**command**](command) directory. 
```
ls command
```

### How to collect the facts from junos devices

The playbook [**pb.collect.facts.yml**](pb.collect.facts.yml) collects the facts on junos devices and save them on Ansible in the directory [**facts**](facts)

Run this command to collect the facts from the junos devices
```
ansible-playbook pb.collect.facts.yml
```

The facts are available in the directory [**facts**](facts)
```
ls facts/
```


### How to collect the junos configuration file from junos devices 

The playbook [**pb.collect.configuration.yml**](pb.collect.configuration.yml) collects the Junos configuration in set, xml, json and text formats, and save the configuration files in the [**directory configuration**](configuration)  

Run this command to collect the junos configuration files for a device/group.  
```
ansible-playbook pb.collect.configuration.yml --limit DC1
```

Run this command to collect the junos configuration files for the whole network
```
ansible-playbook pb.collect.configuration.yml
```

The configuration files are available in the directory [**configuration**](configuration)
```
ls configuration/
```

### How to collect the running configuration on the junos devices and update the golden configuration files

The golden configuration files are the configuration files that will be loaded at the beginning of each demo. 

The playbook [**pb.collect.golden.yml**](pb.collect.golden.yml) collects the running configuration on the junos devices and updates the directory [**golden_configuration**](golden_configuration) with these files.

Run this command to do it for a device/group
```
ansible-playbook pb.collect.golden.yml --limit QFX5110
```

Run this command to do it for the whole network
```
ansible-playbook pb.collect.golden.yml 
```

The golden configuration files are available in the directory [**golden_configuration**](golden_configuration)
```
ls golden_configuration
```


# How to configure the network

### How to overwrite the running configuration on junos devices with their golden confiiguration

The playbook [**pb.configure.golden.yml**](pb.configure.golden.yml) overwrites the running configuration on the junos devices with the files in the directory [**golden_configuration**](golden_configuration).  
You can use it at the beginning of each demo to restore the golden configuration files on the Junos devices.   
Run this command to do it for a device/group
```
ansible-playbook pb.configure.golden.yml --limit QFX10K2-176
```
Run this command to do it for the whole network
```
ansible-playbook pb.configure.golden.yml
```

The playbook [**pb.configure.golden.yml**](pb.configure.golden.yml) backups in the directory [**backup**](backup) the current running configuration from the remote devices before to applying the golden configuration. 
```
ls backup/
```

### How to configure devices with set/delete commands

The playbook [**pb.configure.lines.yml**](pb.configure.lines.yml) configures the junos devices with set/delete commands. 

Edit the playbook [**pb.configure.lines.yml**](pb.configure.lines.yml) to indicate the list of set and delete commands you want to use:
```
vi pb.configure.lines.yml
```

In order to execute the playbook [**pb.configure.lines.yml**](pb.configure.lines.yml) in dry run mode (i.e without commiting the junos configuration)
```
ansible-playbook pb.configure.lines.yml --check
```
How to execute this playbook in dry run mode and also print the diff between the desired state and the actual state 
```
ansible-playbook pb.configure.lines.yml --check --diff --limit QFX10K2-176
```
How to execute this playbook for one device/group
```
ansible-playbook pb.configure.lines.yml --limit DC2
```

The playbook [**pb.configure.lines.yml**](pb.configure.lines.yml) backups in the directory [**backup**](backup) the current running configuration from the remote devices before to applying the configuration change. 
```
ls backup/
```

```
ls backup/
```
How to execute this playbook
```
ansible-playbook pb.configure.lines.yml
```
```
ls backup/
```

### How to configure devices with telemetry
How to read the telemetry template
```
more templates/telemetry.j2
```
How to render the telemetry template locally (i.e without connecting to junos devices)
```
ansible-playbook pb.configure.telemetry.yml --tag render
ls render/telemetry/
```
How to execute this playbook in dry run mode (i.e without commiting the junos configuration)
```
ansible-playbook pb.configure.telemetry.yml --check
```
How to execute this playbook in dry run mode and also print the diff between the desired state and the actual state 
```
ansible-playbook pb.configure.telemetry.yml --check --diff --limit QFX10K2-176
```
How to execute this playbook for one device/group
```
ansible-playbook pb.configure.telemetry.yml --limit QFX10K2-176
```
```
ls backup/
```
How to execute this playbook
```
ansible-playbook pb.configure.telemetry.yml
```
```
ls backup/
```


### How to rollback the running configuration to a previous state

Run this command to rollback 1 the whole network 
```
ansible-playbook pb.rollback.yml --extra-vars rbid=1
```
```
ls rollback/
```
Run this command to rollback 3 the group DC2 
```
ansible-playbook pb.rollback.yml --extra-vars rbid=3 --limit DC2
```
```
ls rollback/
```


# How to audit the network with Ansible

### How to check if some services (netconf, ssh, ftp, telnet ports) are reachable on Junos devices
```
ansible-playbook pb.check.ports.availability.yml
```

### How to check the status of interfaces on Junos devices
```
ansible-playbook pb.check.interfaces.yml
```

### How to check the physical topology 
```
ansible-playbook pb.check.lldp.yml
```

### How to check the BGP states 
```
ansible-playbook pb.check.bgp.yml
```

### How to check from devices operationnal state if desirated vlans are presents
```
ansible-playbook pb.check.vlans.yml
```

### How to collects the facts on junos devices and print them on Ansible
```
ansible-playbook pb.print.facts.yml
```

### How to run all the above tests in one single command
```
ansible-playbook pb.check.all.yml
```

### How to check which devices are not running their golden configuration
Run this command to do it for a device/group
```
ansible-playbook pb.configure.golden.yml --check --limit QFX10K2-176
```
Run this command to do it for the whole network 
```
ansible-playbook pb.configure.golden.yml --check
```
### How to get the diff between theconfiguration running on devices and their golden configuration
Run this command to do it for a device/group
```
ansible-playbook pb.configure.golden.yml --check --diff --limit QFX10K2-176
```
Run this command to do it for the whole network 
```
ansible-playbook pb.configure.golden.yml --check --diff 
```

# How to audit the network using JSNAPy

JSNAPy is a tool to take snapshots, store snapshots, compare snapshots.  
There are 2 JSNAPy workflows:
- take snapshots and compare them against pre defined criteria
- take pre snapshots before any modification and then take post snapshots after modification and then compare them based on test cases

### How to validate there is no active alarms on the devices
run this command to do it
```
jsnapy --snapcheck -f jsnapy/cfg_file_snapcheck_alarms.yml --folder jsnapy
```
if you want to read the snapshots, run this command:
```
ls jsnapy/snapshots
```
### How to see if there are interfaces errors
run this command to do it
```
jsnapy --snapcheck -f jsnapy/cfg_file_snapcheck_interfaces.yml --folder jsnapy
```
if you want to read the snapshots, run this command:
```
ls jsnapy/snapshots
```
### How to validate some BGP details
run this command to do it
```
jsnapy --snapcheck -f jsnapy/cfg_file_snapcheck_bgp.yml --folder jsnapy
```
if you want to read the snapshots, run this command:
```
ls jsnapy/snapshots
```

### Check if the topology changed
take a first snapshot. it will be the source of Truth 
```
jsnapy --snap pre -f jsnapy/cfg_file_check_topology_QFX.yml --folder jsnapy
ls jsnapy/snapshots/
```
later on, if you want to check if the topology changed, take a new snapshot:
```
jsnapy --snap post -f jsnapy/cfg_file_check_topology_QFX.yml --folder jsnapy
ls jsnapy/snapshots/
```
and compare the snapshots:
```
jsnapy --check pre post -f jsnapy/cfg_file_check_topology_QFX.yml --folder jsnapy
```
you can also limit this action to one device, and use the verbose mode:  
```
jsnapy --check pre post -f jsnapy/cfg_file_check_topology_QFX.yml --folder jsnapy -v -t  172.25.90.174
```
Note: as xml output of "show lldp neighbors" is different on QFX and EX, it requires an different parsing. So for EX, use the file cfg_file_check_topology_EX.yml

# Repository structure 

### Ansible inventory file
The ansible inventory file is [**hosts**](hosts) file at the root of the repository.    

### Ansible configuration file
The ansible configuration file is [**ansible.cfg**](ansible.cfg) at the root of the repository.   

### host_vars directory 
The variables are yml files under [**group_vars**](group_vars) and [**host_vars**](host_vars) directories.  
host specific variables under the directory [**host_vars**](host_vars).   

### group_vars directory 
The variables are yml files under [**group_vars**](group_vars) and [**host_vars**](host_vars) directories.  
group related variables are yml files under the directory [**group_vars**](group_vars)

### templates directory
The directory [**templates**](templates) has the jinja templates

### render directory
The directory [**render**](render) has the files generated from the jinja templates and variables

### Ansible Playbooks
The ansible playbooks are at the root of the repository.  
All playbooks are named **pb.*.yml**      

##### Ansible Playbooks to configure the network
- [**pb.configure.golden.yml**](pb.configure.golden.yml) playbook overwrites the running configuration on the junos devices with the files in the directory [**golden_configuration**](golden_configuration). 
- [**pb.configure.lines.yml**](pb.configure.lines.yml) playbook configures junos devices with set/delete commands
- [**pb.configure.telemetry.yml**](pb.configure.telemetry.yml) playbook configures junos devices with telemetry
- [**pb.rollback.yml**](pb.rollback.yml) playbook performs a rollback on junos devices.

##### Ansible Playbooks to collect data from the network
- [**pb.collect.configuration.yml**](pb.collect.configuration.yml) playbook performs a configuration backup of the network and save the configuration files in the directory [**configuration**](configuration)
- [**pb.collect.golden.yml**](pb.collect.golden.yml) playbook collects the running configuration on the junos devices and updates the directory [**golden_configuration**](golden_configuration) with these files.
- [**pb.collect.commands.output.yml**](pb.collect.commands.output.yml) playbook runs junos show commands and save the output on Ansible 
- [**pb.collect.cli.output.yml**](pb.collect.cli.output.yml) playbook runs junos show commands and save the output on Ansible. This playbook use the show commands in the file [**cli.yml**](cli.yml)
- [**pb.collect.facts.yml**](pb.collect.facts.yml) playbook collects the facts on junos devices and save them on Ansible in the directory [**facts**](facts)

##### Ansible Playbooks to audit the network
- [**pb.check.all.yml**](pb.check.all) playbook include these playbooks:
 - [**pb.check.ports.availability.yml**](pb.check.ports.availability.yml) playbook checks if Ansible can connect on some ports on Junos devices (ssh, telnet, ftp, netconf)
 - [**pb.check.interfaces.yml**](pb.check.interfaces.yml) playbook checks the status of the interfaces on Junos devices
 - [**pb.check.lldp.yml**](pb.check.lldp.yml) playbook check the physical topology 
 - [**pb.check.bgp.yml**](pb.check.bgp.yml) playbook check the BGP states 
 - [**pb.check.vlans.yml**](pb.check.vlans.yml) playbook check from devices operationnal state if desirated vlans are presents
 - [**pb.print.facts.yml**](pb.print.facts.yml) playbook collects the facts on junos devices and print them on Ansible

##### Other Ansible Playbooks
- [**pb.generate.variables.structure.yml**](pb.generate.variables.structure.yml) playbook was used at the beginning of the project to create some of the directories and files used to define yaml variables. 
- [**pb.generate.jsnapy.inventory.yml**](pb.generate.jsnapy.inventory.yml) playbook creates the JSNAPy inventory file [**devices.yml**](devices.yml) based on the Ansible inventory file [**hosts**](hosts)


### cli directory 
The directory [**cli**](cli) has the output of the Junos show commands from the playbook [**pb.collect.cli.output.yml**](pb.collect.cli.output.yml)

### command directory 
The directory [**command**](command) has the output of the Junos show commands from the playbook [**pb.collect.commands.output.yml**](pb.collect.commands.output.yml) 

### facts directory
The directory [**facts**](facts) has the Junos facts collected by the playbook [**pb.collect.facts.yml**](pb.collect.facts.yml) 

### rollback directory
The directory [**rollback**](rollback) has the Junos configuration diffs from rollbacks done with ansible playbook [**pb.rollback.yml**](pb.rollback.yml) 

### backup directory
The directory [**backup**](backup) has the junos configuration files automatically backed up by the playbooks: 
  - [**pb.configure.lines.yml**](pb.configure.lines.yml) 
  - [**pb.configure.golden.yml**](pb.configure.golden.yml)
  - [**pb.configure.telemetry.yml**](pb.configure.telemetry.yml)

### configuration directory
The directory [**configuration**](configuration) has the junos configuration files backed up when we ran the playbook [**pb.collect.configuration.yml**](pb.collect.configuration.yml) 

### golden directory
The directory [**golden_configuration**](golden_configuration) has the junos configuration files we need to push on the junos devices before to start the demo. 
- The playbook [**pb.collect.golden.configuration.yml**](pb.collect.golden.configuration.yml) collects the running configuration on the junos devices and updates the directory [**ebgp_underlay_evpn_vxlan_overlay**](/golden_configuration/ebgp_underlay_evpn_vxlan_overlay/) with these files.
- The playbook [**pb.configure.golden.yml**](pb.configure.golden.yml) overwrites the running configuration on the junos devices with the files in the directory [**ebgp_underlay_evpn_vxlan_overlay**](/golden_configuration/ebgp_underlay_evpn_vxlan_overlay/)

### fragments directory
The directory [**fragments**](fragments) is used by the playbook [**pb.generate.jsnapy.inventory.yml**](pb.generate.jsnapy.inventory.yml) to create the JSNAPy inventory file [**devices.yml**](devices.yml) based on the Ansible inventory file [**hosts**](hosts).  
The directory [**fragments**](fragments)  doesnt contains the JSNAPy inventory file [**devices.yml**](devices.yml) itself.

### python directory
The directory [**python**](python) has the python scripts
- The file [**inventory.py**](python/inventory.py) creates a python list of devices ip address based on the ansible inventory file [**hosts**](hosts)
- The file [**credentials.py**](python/credentials.py) get the devices username and password from the ansible variables file  [**credentials.yml**](/group_vars/JUNOS/credentials.yml)
- The file [**locate.mac.address.py**](python/locate.mac.address.py) indicates where is locate a given mac address in the network.

### jsnapy directory
The directory [**jsnapy**](jsnapy) has the jsnapy content:
- The directory [**jsnapy**](jsnapy) has the JSNAPy configuration files. They are named **cfg_file_*.yml**.
    - [**cfg_file_check_topology_EX.yml**](jsnapy/cfg_file_check_topology_EX.yml) jsnapy file checks if the topology changed between 2 snapshots
    - [**cfg_file_check_topology_QFX.yml**](jsnapy/cfg_file_check_topology_QFX.ym) jsnapy file checks if the topology changed between 2 snapshots 
    - [**cfg_file_snapcheck_alarms.yml**](jsnapy/cfg_file_snapcheck_alarms.yml) jsnapy file checks if they are active alarms
    - [**cfg_file_snapcheck_bgp.yml**](jsnapy/cfg_file_snapcheck_bgp.yml) jsnapy file checks some BGP details
    - [**cfg_file_snapcheck_interfaces.yml**](jsnapy/cfg_file_snapcheck_interfaces.yml) jsnapy file checks if there are interfaces errors  
- The directory [**snapshots**](jsnapy/snapshots) has the snapshots taken by jsnapy
- The directory [**testfiles**](jsnapy/testfiles) has the JSNAPy inventory file [**devices.yml**](jsnapy/testfiles/devices.yml). It is created with the playbook [**pb.generate.jsnapy.inventory.yml**](pb.generate.jsnapy.inventory.yml), based on the Ansible inventory file [**hosts**](hosts) and on Ansible variables file for devices credentials  [**credentials.yml**](/group_vars/JUNOS/credentials.yml)
- The directory [**testfiles**](jsnapy/testfiles) has also the testfiles used by jsnapy. They are named **test_file_*.yml**. 
    - [**test_file_check_topology_EX.yml**](jsnapy/testfiles/test_file_check_topology_EX.yml)
    - [**test_file_check_topology_QFX.yml**](jsnapy/testfiles/test_file_check_topology_QFX.yml)
    - [**test_file_snapcheck_alarms.yml**](jsnapy/testfiles/test_file_snapcheck_alarms.yml)
    - [**test_file_snapcheck_bgp.yml**](jsnapy/testfiles/test_file_snapcheck_bgp.yml)
    - [**test_file_snapcheck_interfaces.yml**](jsnapy/testfiles/test_file_snapcheck_interfaces.yml)
    


# Looking for help 

### Looking for help with Junos automation:

https://github.com/ksator?tab=repositories  
https://gitlab.com/users/ksator/projects  
https://gist.github.com/ksator/  

### Looking for more EVPN-VXLAN automation examples

You can refer to these projects:  
https://github.com/JNPRAutomate/ansible-junos-evpn-vxlan  
https://github.com/ksator/EVPN_DCI_automation  
