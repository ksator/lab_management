
# Looking for help with Ansible? 

This [repository](https://github.com/ksator/ansible-training-for-junos-automation) has many examples about junos automation using Ansible

## How to install Ansible

Run these commands on Ubuntu 16.04:
```
sudo -s
apt-get update
apt-get install -y python-dev libxml2-dev python-pip libxslt1-dev build-essential libssl-dev libffi-dev git
pip install junos-eznc jxmlease wget jsnapy ansible requests ipaddress cryptography==1.2.1 
ansible-galaxy install Juniper.junos
```

# How to use this repo:

## How to get the remote content locally:

```
git clone http://172.25.90.133/root/PoC-80.git
cd PoC-80/
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

## How to backup locally junos configuration

```
ansible-playbook pb.backup.configuration.yml
ls backup/
```

## How to pass show commands on junos devices

```
ansible-playbook pb.collect.cli.output.yml
ls cli
```
```
ansible-playbook pb.collect.commands.output.yml
ls command
```


