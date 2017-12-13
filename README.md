
# Looking for help with Ansible? 

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

# How to get the remote content locally

```
sudo -s
git clone http://172.25.90.133/root/PoC-80.git
cd PoC-80/
```
# How to use this repo:

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

## How to rollback a device or a network
```
ansible-playbook pb.rollback.yml --extra-vars rbid=1
ls rollback/
```
```
ansible-playbook pb.rollback.yml --extra-vars rbid=3 --limit DC2
ls rollback/
```

