def ansible_credentials_to_python_credentials(): 
	import yaml
	from pprint import pprint as pp

	credentials_file = open('group_vars/JUNOS/credentials.yml', "r")
	credentials_file_content = credentials_file.read()
	credentials_file_content_in_yaml = yaml.load(credentials_file_content)

	'''
	pp(credentials_file_content_in_yaml)
	type(credentials_file_content_in_yaml)
	credentials_file_content_in_yaml
	credentials_file_content_in_yaml['credentials']['username']
	credentials_file_content_in_yaml['credentials']['password']
	'''

	user = credentials_file_content_in_yaml['credentials']['username']
	password = credentials_file_content_in_yaml['credentials']['password']

	credentials = {'user': user, 'password': password}
	return credentials

