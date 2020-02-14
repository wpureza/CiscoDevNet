import json
import os


# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, "interfaces.json")) as file:
    # TODO: Parse the contents of the JSON file into a variable
    json_interfaces = json.loads(file.read())
    # print(json.dumps(json_interfaces, sort_keys=True, indent=4))
    interfaces = json_interfaces["ietf-interfaces:interfaces"]['interface']

# TODO: Loop through the interfaces in the JSON data and print out each
# interface's name, ip, and netmask.
print("{0:42}{1:17}{2:12}".format("Name", "IP", "Netmask"))
for nic in interfaces:
    print("{0:42}{1:17}{2:12}".format(nic['name'], nic['ietf-ip:ipv4']['address'][0]['ip'], nic['ietf-ip:ipv4']['address'][0]['netmask']))

