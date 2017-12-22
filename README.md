# What to find in this repository

Junos automation content for data center network fabric.  
It is used to manage a lab.  
It is based on:    
- Junos devices
- Ansible, PyEZ, JSNAPy

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
- [**pb.generate.variables.structure.yml**](pb.generate.variables.structure.yml) playbook was used at the beginning of the project to create some of the directories and files used to define yaml variables. 

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
- The playbook [**pb.collect.golden.configuration.yml**](pb.collect.golden.configuration.yml) collects the running configuration on the junos devices and updates the directory [**/golden_configuration/ebgp_underlay_evpn_vxlan_overlay/**](/golden_configuration/ebgp_underlay_evpn_vxlan_overlay/) with these files.
- The playbook [**pb.configure.golden.yml**](pb.configure.golden.yml) overwrites the running configuration on the junos devices with the files in the directory [**/golden_configuration/ebgp_underlay_evpn_vxlan_overlay/**](/golden_configuration/ebgp_underlay_evpn_vxlan_overlay/)

### python directory
The directory [**python**](python) has the python scripts
- The file [**python/inventory.py**](python/inventory.py) create a python list of devices ip address based on the ansible inventory file [**hosts**](hosts)
- The file [**python/locate.mac.address.py**](python/locate.mac.address.py) indicates where is locate a given mac address in the network.

### jsnapy directory
The directory [**jsnapy**](jsnapy) has the jsnapy content
- The directory [**jsnapy/snapshots**](jsnapy/snapshots) has the snapshots taken by jsnapy
- The directory [**jsnapy/testfiles**](jsnapy/testfiles) has the testfiles taken by jsnapy


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

# How to collect data from the network 

### How to collect the facts from junos devices
Run this command to collect the facts
```
ansible-playbook pb.collect.facts.yml
```
The facts are available in the facts directory
```
ls facts/
```

### How to pass show commands on junos devices and collect the output
Edit the show commands you want to use
```
vi cli.yml
```
Run this command
```
ansible-playbook pb.collect.cli.output.yml
```
The commands output is available in the cli directory
```
ls cli
```
### How to pass show commands on junos devices and collect the output (alternative automation content)
Edit the show commands you want to use
```
vi pb.collect.commands.output.yml
```
Run this command
```
ansible-playbook pb.collect.commands.output.yml
```
The commands output is available in the command directory
```
ls command
```

### How to collect the junos configuration file from junos devices 
Run this command to collect the junos configuration file for a device/group
```
ansible-playbook pb.collect.configuration.yml --limit DC1
ls configuration/
```
Run this command to collect the junos configuration file for the whole network
```
ansible-playbook pb.collect.configuration.yml
ls configuration/
```

### How to collect the running configuration on the junos devices and update the golden configuration files (the initial configuration files that will be used at the beginning of the next demo) 

Run this command to do it for a device/group
```
ansible-playbook pb.collect.golden.yml --limit QFX5110
ls golden_configuration
```
Run this command to do it for the whole network
```
ansible-playbook pb.collect.golden.yml 
ls golden_configuration
```


# How to configure the newtwork

### How to overwrite the running configuration on junos devices with their golden confiiguration (i.e how to restore the initial configuration files at the beginning of each demo)
Run this command to do it for a device/group
```
ansible-playbook pb.configure.golden.yml --limit QFX10K2-176
```
```
ls backup/
```
Run this command to do it for the whole network
```
ansible-playbook pb.configure.golden.yml
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
### How to configure devices with set/delete commands
How to edit the set/delete commands you want to use
```
vi pb.configure.lines.yml
```
How to execute this playbook in dry run mode (i.e without commiting the junos configuration)
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


# How to audit the network

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

# python

# Looking for help 

### Looking for help with Junos automation:

https://github.com/ksator?tab=repositories  
https://gitlab.com/users/ksator/projects  
https://gist.github.com/ksator/  

### Looking for more EVPN-VXLAN automation examples

You can refer to these projects:  
https://github.com/JNPRAutomate/ansible-junos-evpn-vxlan  
https://github.com/ksator/EVPN_DCI_automation  
