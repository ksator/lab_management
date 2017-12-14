
# Looking for help with Ansible

This [repository](https://github.com/ksator/ansible-training-for-junos-automation) has many examples about junos automation using Ansible

# How to install Ansible

This repository has been tested using Ansible 2.4.2.0  

Run these commands on Ubuntu 16.04:
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

# How to get locally the content of the remote repository

```
sudo -s
git clone http://172.25.90.133/root/PoC-80.git
cd PoC-80/
```
# Repository structure 

- The ansible inventory file is [**hosts**](http://172.25.90.133/root/PoC-80/blob/master/hosts) file at the root of the repository.    

- The ansible configuration file is [**ansible.cfg**](http://172.25.90.133/root/PoC-80/blob/master/ansible.cfg) at the root of the repository.   

- variables are yml files under [**group_vars**](http://172.25.90.133/root/PoC-80/tree/master/group_vars) and [**host_vars**](http://172.25.90.133/root/PoC-80/tree/master/host_vars) directories.   
  - host specific variables under the directory [**host_vars**](http://172.25.90.133/root/PoC-80/tree/master/host_vars).   
  - group related variables are yml files under the directory [**group_vars**](http://172.25.90.133/root/PoC-80/tree/master/group_vars)

- The ansible playbooks are at the root of the repository. All playbooks are named pb.*.yml      
  - [**pb.backup.configuration.yml**](http://172.25.90.133/root/PoC-80/blob/master/pb.backup.configuration.yml) playbook performs a configuration backup of the network
  - [**pb.configure.lines.yml**](http://172.25.90.133/root/PoC-80/blob/master/pb.configure.lines.yml) playbook configures junos devices with set/delete commands
  - [**pb.rollback.yml**](http://172.25.90.133/root/PoC-80/blob/master/pb.rollback.yml) playbook performs a rollback on junos devices.
  - [**pb.check.connectivity.yml**](http://172.25.90.133/root/PoC-80/blob/master/pb.check.connectivity.yml) playbook checks if Ansible can connect on SSH and NETCONF ports on Junos devices
  - [**pb.collect.cli.output.yml**](http://172.25.90.133/root/PoC-80/blob/master/pb.collect.cli.output.yml) playbook runs junos show commands and save the output on Ansible. This playbook use the commands in the file [**cli.yml**](http://172.25.90.133/root/PoC-80/blob/master/cli.yml)
  - [**pb.collect.commands.output.yml**](http://172.25.90.133/root/PoC-80/blob/master/pb.collect.commands.output.yml) playbook runs junos show commands and save the output on Ansible 
  - [**pb.print.facts.yml**](http://172.25.90.133/root/PoC-80/blob/master/pb.print.facts.yml) playbook collects the facts on junos devices and print them on Ansible
  - [**pb.collect.facts.yml**](http://172.25.90.133/root/PoC-80/blob/master/pb.collect.facts.yml) playbook collects the facts on junos devices and save them on Ansible 

- The junos configuration files are backed up in the directory [**configuration_backup**](http://172.25.90.133/root/PoC-80/tree/master/configuration_backup) by the playbook [**pb.backup.configuration.yml**](http://172.25.90.133/root/PoC-80/blob/master/pb.backup.configuration.yml) 

- The junos configuration files are backed up in the directory [**backup**](http://172.25.90.133/root/PoC-80/tree/master/backup) by the playbook [**pb.configure.lines.yml**](http://172.25.90.133/root/PoC-80/blob/master/pb.configure.lines.yml) 

- The Junos configuration diffs from rollbacks done with ansible playbook [**pb.rollback.yml**](http://172.25.90.133/root/PoC-80/blob/master/pb.rollback.yml) are in the directory [**rollback**](http://172.25.90.133/root/PoC-80/tree/master/rollback) 

- The Junos facts are saved in the directory [facts](http://172.25.90.133/root/PoC-80/tree/master/facts) by the playbook [**pb.collect.facts.yml**](http://172.25.90.133/root/PoC-80/blob/master/pb.collect.facts.yml) 

- The Junos commands output from the playbook [**pb.collect.cli.output.yml**](http://172.25.90.133/root/PoC-80/blob/master/pb.collect.cli.output.yml) are saved in the directory [**cli**](http://172.25.90.133/root/PoC-80/tree/master/cli)

- The Junos commands output from the playbook [**pb.collect.commands.output.yml**](http://172.25.90.133/root/PoC-80/blob/master/pb.collect.commands.output.yml) are saved in the directory [**command**](http://172.25.90.133/root/PoC-80/tree/master/command)


# How to use this repo

```
sudo -s
```

## How to check if ssh and netconf ports are reachable on Junos devices
```
ansible-playbook pb.check.connectivity.yml
```

## How to retrieves facts from junos devices: 

```
ansible-playbook pb.collect.facts.yml
ls facts/
```
```
ansible-playbook pb.print.facts.yml
```

## How to backup the junos configuration on the Ansible server

```
ansible-playbook pb.backup.configuration.yml
ls configuration_backup/
```

## How to pass show commands on junos devices

```
vi cli.yml
ansible-playbook pb.collect.cli.output.yml
ls cli
```
```
ansible-playbook pb.collect.commands.output.yml
ls command
```

## How to configure devices with set/delete commands
```
vi pb.configure.lines.yml
ansible-playbook pb.configure.lines.yml --check
ansible-playbook pb.configure.lines.yml --check --diff --limit QFX10K2-36Q-176
ansible-playbook pb.configure.lines.yml
ls backup/
```

## How to rollback a device or a network
```
ansible-playbook pb.rollback.yml --extra-vars rbid=1
ls rollback/
```
```
ansible-playbook pb.rollback.yml --extra-vars rbid=3 --limit DC2
ls rollback/
```

